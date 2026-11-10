from models import MediaItem, Playlist

playlist = Playlist("Riya's Evening Mix")

playlist.add_item(MediaItem("Blinding Lights", "The Weeknd", "Song", 200, 4.8))
playlist.add_item(MediaItem("Data Skeptic", "Kyle Polich", "Podcast", 1875, 4.5))
playlist.add_item(MediaItem("Kesariya", "Arijit Singh", "Song", 268, 4.6))
playlist.add_item(MediaItem("Syntax Tasty Treats", "Wes Bos", "Podcast", 1260, 4.1))

print("=== Milestone 3: Playlist Report ===")
print("Application    :", MediaItem.app_name)
print("Playlist name  :", playlist.playlist_name)
print("Playlist size  :", len(playlist), "items")
print("Total duration :", playlist.total_duration(), "seconds")
print("Top-rated item :", playlist.top_rated())
print()
playlist.display_playlist()
