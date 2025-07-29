import json
import os
import subprocess
import re

def normalize_date(date_str):
    try:
        mm, dd, yy = date_str.strip().split('/')
        mm = mm.zfill(2)
        dd = dd.zfill(2)
        yy = yy.zfill(2)
        return f"{mm}/{dd}/{yy}"
    except ValueError:
        raise ValueError("Date must be in MM/DD/YY format.")

def get_next_index(directory="."):
    max_index = -1
    for filename in os.listdir(directory):
        match = re.fullmatch(r"(\d+)\.json", filename)
        if match:
            idx = int(match.group(1))
            if idx > max_index:
                max_index = idx
    return max_index + 1

def create_blog_entry():
    title = input("Input blog title: ")

    while True:
        try:
            raw_date = input("Input date (MM/DD/YY): ")
            date = normalize_date(raw_date)
            break
        except ValueError as e:
            print(f"Invalid input: {e}")

    print("Input blog content (end it with END_BLOG_ENTRY):")
    content_lines = []
    while True:
        line = input()
        if line == "END_BLOG_ENTRY":
            break
        content_lines.append(line)
    content = "\n".join(content_lines)

    content = content.replace('"', "\"")

    entry = {
        "TITLE": title,
        "DATE": date,
        "CONTENT": content
    }

    preview_text = input("Preview text? [y/n]: ")
    if preview_text.lower() == 'y':
        print("Input preview text: (end it with END_BLOG_ENTRY):")
        content_lines = []
        while True:
            line = input()
            if line == "END_BLOG_ENTRY":
                break
            content_lines.append(line)
        preview = "\n".join(content_lines)
        entry["PREVIEW"] = preview

    index = get_next_index()
    filename = f"{index}.json"

    with open(filename, 'w', encoding='utf-8') as json_file:
        json.dump(entry, json_file, indent=4)

    print(f"Blog entry saved as {filename}")
    
    try:
        subprocess.run(["python", "build_blogs.py"], check=True)
        # subprocess.run(["python", "generate_rss.py"], check=True)
    except Exception as e:
        print(f"Error running build_blogs.py or generate_rss.py: {e}")

    input("Press Enter to exit...")

if __name__ == "__main__":
    create_blog_entry()
