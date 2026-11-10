# main.py - Milestone 5: listening history with file handling
from models import MediaItem
from media_utils import seconds_to_hms

HISTORY_FILE = "listening_history.txt"


def save_history(item, filename=HISTORY_FILE):
    # append one completed record, fields separated by |
    with open(filename, "a") as file:
        file.write(f"{item.title}|{item.media_type}|{item.duration_sec}|{item.rating}\n")


def load_history(filename=HISTORY_FILE):
    records = []
    try:
        with open(filename, "r") as file:
            line_no = 0
            line = file.readline()
            while line != "":
                line_no += 1
                try:
                    title, media_type, duration, rating = line.strip().split("|")
                    duration = int(duration)          # ValueError if not a number
                    rating = float(rating)
                    if duration <= 0 or rating < 1 or rating > 5:
                        raise ValueError("value out of range")
                    records.append((title, media_type, duration, rating))
                except ValueError as error:
                    print(f"  Line {line_no} skipped ({error}): {line.strip()}")
                if line_no == 1:
                    print("  file.tell() after first line:", file.tell())
                line = file.readline()
    except FileNotFoundError:
        print(f"  File '{filename}' not found.")
    return records


# create one completed record from user input and save it
title = input("Title: ")
creator = input("Creator: ")
media_type = input("Type (Song/Podcast): ")
duration = int(input("Duration (sec): "))
rating = float(input("Rating (1-5): "))
save_history(MediaItem(title, creator, media_type, duration, rating))

print("\nReading history file:")
records = load_history()
print("Valid records:", len(records))
for title, media_type, duration, rating in records:
    print(f"  {title} | {media_type} | {seconds_to_hms(duration)} | {rating}/5")

print("\nTrying to read a missing file:")
load_history("old_history.txt")
