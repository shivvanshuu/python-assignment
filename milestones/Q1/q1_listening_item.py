# Milestone 1 - Represent and Analyse One Listening Item
# COM-501 Python Programming | Digital Playlist and Listening Analytics System

print("=== Milestone 1: Listening Item Analyser ===")

# (a) Input the details of one song / podcast episode (input() returns str)
listener = input("Enter listener name            : ").strip()
title = input("Enter title                    : ").strip()
creator = input("Enter creator                  : ").strip()
media_type = input("Enter media type (Song/Podcast): ").strip()
duration_text = input("Enter duration (seconds)       : ")
rating_text = input("Enter rating (out of 5)        : ")

# (b) Convert to numeric data types and display the Python data types
duration_sec = int(duration_text)      # whole number of seconds
rating = float(rating_text)            # decimal rating, e.g. 4.5

print("\n--- Python data types ---")
print("duration before conversion :", type(duration_text))
print("duration after conversion  :", type(duration_sec))
print("rating before conversion   :", type(rating_text))
print("rating after conversion    :", type(rating))

# (c) Convert seconds into minutes and remaining seconds using // and %
minutes = duration_sec // 60
seconds = duration_sec % 60

# (d) 3-character media code using string slicing
media_code = media_type[:3].upper()

# (d) Neat labelled output
print("\n========== LISTENING ITEM REPORT ==========")
print(f"Listener   : {listener}")
print(f"Title      : {title}")
print(f"Creator    : {creator}")
print(f"Media Type : {media_type}")
print(f"Duration   : {duration_sec} seconds = {minutes} min {seconds} sec")
print(f"Rating     : {rating} / 5")
print(f"Media Code : {media_code}")
print("===========================================")
