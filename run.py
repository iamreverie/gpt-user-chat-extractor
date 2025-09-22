import json
import os
import argparse
from datetime import datetime, timezone
from dateutil import parser as dateparser


def extract_prompts(json_path, output_path, starting_date=None):
    with open(json_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    if not isinstance(data, list):
        raise ValueError("JSON structure not supported: root must be a list of conversations.")

    if starting_date:
        filter_date = dateparser.parse(starting_date)
        if filter_date.tzinfo is None:
            filter_date = filter_date.replace(tzinfo=timezone.utc)
    else:
        filter_date = None

    entries = []
    for conversation in data:
        title = conversation.get("title", "Untitled Conversation")
        messages = conversation.get("mapping", {}).values()
        prompts = []
        for msg in messages:
            if not isinstance(msg, dict):
                continue
            message_doc = msg.get("message")
            if not isinstance(message_doc, dict):
                continue
            author_doc = message_doc.get("author")
            if not isinstance(author_doc, dict):
                continue
            if author_doc.get("role") == "user":
                create_time = message_doc.get("create_time")
                parts = message_doc.get("content", {}).get("parts", [])
                if not create_time or not parts:
                    continue
                # content extraction: only join if all parts are strings, else safely cast
                if isinstance(parts, list):
                    part_strings = [str(p) for p in parts if isinstance(p, (str, int, float))]
                    content_joined = " ".join(part_strings).strip()
                else:
                    content_joined = str(parts).strip()
                if not content_joined:
                    continue
                # use timezone-aware datetime as per the deprecation warning
                dt = datetime.fromtimestamp(create_time, timezone.utc)
                if filter_date and dt < filter_date:
                    continue
                prompts.append(f"{dt.strftime('%Y-%m-%d %H:%M:%S')} - {content_joined}")

        if prompts:
            entries.append((title, prompts))

    with open(output_path, 'a', encoding='utf-8') as out_file:
        for title, prompts in entries:
            out_file.write(f"[{title}]\n")
            for p in prompts:
                out_file.write(f"{p}\n")
            out_file.write("\n")
    total_prompts = sum(len(prompts) for _, prompts in entries)
    print(f"Extracted {total_prompts} prompts.")


def main():
    parser = argparse.ArgumentParser(description="Extract user prompts from ChatGPT JSON export.")
    parser.add_argument('json_file', type=str, help='Full path to the ChatGPT JSON file')
    parser.add_argument('output_file', type=str, help='Path to the output file')
    parser.add_argument('starting_date', nargs='?', default=None, help='Optional: start collecting from this date (YYYY-MM-DD)')
    args = parser.parse_args()

    extract_prompts(args.json_file, args.output_file, args.starting_date)

if __name__ == "__main__":
    main()
