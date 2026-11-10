# main.py - Milestone 4
import time
from models import MediaItem, Playlist
from media_utils import seconds_to_hms, filter_by_rating, summarize_by_type

playlist = Playlist("Riya's Evening Mix")
playlist.add_item(MediaItem("Blinding Lights", "The Weeknd", "Song", 200, 4.8))
playlist.add_item(MediaItem("Data Skeptic", "Kyle Polich", "Podcast", 1875, 4.5))
playlist.add_item(MediaItem("Shape of You", "Ed Sheeran", "Song", 234, 3.9))
playlist.add_item(MediaItem("Syntax Tasty Treats", "Wes Bos", "Podcast", 1260, 4.1))


def show_high_rated(items):
    good = filter_by_rating(items)        # default min_rating = 4.0
    good = sorted(good, key=lambda item: item.rating, reverse=True)   # lambda
    print("Items rated 4.0 or above (highest first):")
    for item in good:
        print(" ", item)


def show_summary(items):
    start = time.perf_counter()
    summary = summarize_by_type(items)
    for media_type, data in summary.items():
        time_text = seconds_to_hms(data["total_seconds"])
        print(f"{media_type:<8}: {data['count']} item(s), {time_text}, "
              f"average rating {data['avg_rating']}")
    elapsed = time.perf_counter() - start
    print(f"Summary generated in {elapsed:.6f} seconds")


# menu choices mapped to functions
menu = {"1": show_high_rated, "2": show_summary}

print("1. High rated items\n2. Summary by type\n0. Exit")
while True:
    choice = input("\nEnter choice: ")
    if choice == "0":
        break
    elif choice in menu:
        menu[choice](playlist.items)      # call the function through the dictionary
    else:
        print("Invalid choice")
