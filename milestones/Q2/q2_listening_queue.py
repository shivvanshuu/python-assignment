# Milestone 2 - Build a Multi-Item Listening Queue

queue = []                 # list of dictionaries
unique_creators = set()    # each creator is stored only once

print("=== Milestone 2: Listening Queue ===")
print("Type DONE as the title to finish.\n")

while True:
    title = input("Title (or DONE)      : ")
    if title.upper() == "DONE":
        break
    creator = input("Creator              : ")
    media_type = input("Type (SONG/PODCAST)  : ").upper()
    duration = int(input("Duration (sec)       : "))
    rating = float(input("Rating (1-5)         : "))

    # reject invalid records and go to the next one
    if duration <= 0:
        print("  Rejected: duration must be greater than 0.\n")
        continue
    if rating < 1 or rating > 5:
        print("  Rejected: rating must be between 1 and 5.\n")
        continue

    # classify by duration
    if duration <= 300:
        category = "Quick"
    elif duration <= 1800:
        category = "Standard"
    else:
        category = "Long-form"

    queue.append({"title": title, "creator": creator, "type": media_type,
                  "duration": duration, "rating": rating, "category": category})
    unique_creators.add(creator)
    print(f"  Added: {title} [{category}]\n")

print("\n========== QUEUE SUMMARY ==========")
if len(queue) == 0:
    print("No valid items entered.")
else:
    total = 0
    counts = {"Quick": 0, "Standard": 0, "Long-form": 0}
    best = queue[0]
    for item in queue:
        total += item["duration"]
        counts[item["category"]] += 1
        if item["rating"] > best["rating"]:
            best = item

    print(f"Total listening time : {total} s ({total // 60} min {total % 60} s)")
    for name in counts:
        print(f"{name:<10} items      : {counts[name]}")
    print(f"Highest-rated item   : {best['title']} ({best['rating']})")
    print(f"Unique creators      : {len(unique_creators)}")
