# FIRST (faulty) version of the history loader - no exception handling
def load_history_v1(filename):
    records = []
    with open(filename) as file:
        for line in file:
            title, media_type, duration, rating = line.strip().split("|")
            records.append({"title": title, "type": media_type,
                            "duration": int(duration), "rating": float(rating)})
    return records


records = load_history_v1("listening_history.txt")
print("Loaded", len(records), "records")
for record in records:
    print(record)
