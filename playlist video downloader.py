import os
import re
from pytube import Playlist, YouTube

# Define the URL of the YouTube playlist
playlist_url = "https://www.youtube.com/playlist?list=PLqinEaadXCHafv_XpkNJJ_HPLtMpzRgjq"

# Define the path of the folder where you want to save the videos
folder_path = "/content/downloads"

# Create the folder if it doesn't exist
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Create a playlist object
playlist = Playlist(playlist_url)

# Set the video resolution to the best available
playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")

# Iterate over each video in the playlist
for video_url in playlist.video_urls:
    try:
        # Create a YouTube object for the video
        youtube = YouTube(video_url)

        # Get the best available stream
        video = youtube.streams.get_highest_resolution()

        # Download the video
        video.download(folder_path)

        print(f"Downloaded: {video.title}")

    except Exception as e:
        print(f"Error downloading video: {video_url}")
        print(str(e))
