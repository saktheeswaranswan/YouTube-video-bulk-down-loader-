import pytube

def download_youtube_video(video_url, folder_name):
    """Downloads a YouTube video in 720p resolution to a specified folder.

    Args:
        video_url: The URL of the YouTube video to download.
        folder_name: The name of the folder to download the video to.
    """

    yt = pytube.YouTube(video_url)
    video_stream = yt.streams.filter(res="720p", progressive=True).first()
    
    if video_stream:
        video_stream.download(folder_name)
        print(f"Video '{yt.title}' downloaded successfully!")
    else:
        print(f"No suitable video stream found for '{yt.title}'.")

if __name__ == "__main__":
    video_urls = [
        "https://www.youtube.com/watch?v=e8zWBzv_IEw",
        "https://www.youtube.com/watch?v=kHa2QFmqcEM",
        "https://www.youtube.com/watch?v=6ooosZ6R7fQ",
        "https://www.youtube.com/watch?v=Hvzb376xMjA",
        "https://www.youtube.com/watch?v=Jch71tJLsJQ",
        "https://www.youtube.com/watch?v=idi6aoIOHGk",
        "https://www.youtube.com/watch?v=mpE_VoLzClk"
    ]
    folder_name = "youtubedeos"
    
    for video_url in video_urls:
        download_youtube_video(video_url, folder_name)
