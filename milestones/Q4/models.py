# Milestone 3 - Playlist modelled with two collaborating classes


class MediaItem:
    """A single song or podcast episode."""

    app_name = "Digital Playlist & Listening Analytics System"   # class variable

    def __init__(self, title, creator, media_type, duration_sec, rating):
        self.title = title
        self.creator = creator
        self.media_type = media_type
        self.duration_sec = duration_sec
        self.rating = rating

    def __str__(self):
        return (f"[{self.media_type}] {self.title} by {self.creator} | "
                f"{self.duration_sec} s | Rating {self.rating}/5")


class Playlist:
    """A named collection of MediaItem objects (composition: Playlist HAS-A list of items)."""

    def __init__(self, playlist_name):
        self.playlist_name = playlist_name
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def total_duration(self):
        total = 0
        for item in self.items:
            total += item.duration_sec
        return total

    def top_rated(self):
        if len(self.items) == 0:
            return None
        best = self.items[0]
        for item in self.items:
            if item.rating > best.rating:
                best = item
        return best

    def display_playlist(self):
        print(f"Playlist: {self.playlist_name}  ({MediaItem.app_name})")
        for number, item in enumerate(self.items, start=1):
            print(f"  {number}. {item}")

    def __len__(self):
        return len(self.items)
