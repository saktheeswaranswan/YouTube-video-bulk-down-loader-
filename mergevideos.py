!pip install imageio-ffmpeg
# Install moviepy and the required dependencies
!pip install moviepy
!apt-get install -y ffmpeg
import os
import imageio_ffmpeg as ffmpeg
from moviepy.editor import VideoFileClip, clips_array

# Define the path to the folder containing your videos
video_folder = '/content/downloads'

# Get a list of all .mp4 files in the folder
video_files = [f for f in os.listdir(video_folder) if f.endswith('.mp4')]

# Create a list to store video clips
video_clips = []

# Load each video file and append it to the list
for video_file in video_files:
    video_path = os.path.join(video_folder, video_file)
    video_clip = VideoFileClip(video_path)

    # Resize the video to 720p if it's not already
    if video_clip.size != (1280, 720):
        video_clip = video_clip.resize(height=720)

    video_clips.append(video_clip)

# Concatenate the video clips horizontally
final_video = clips_array([video_clips])

# Define the output file path for the merged video
output_path = '/content/merged_video.mp4'

# Write the merged video to the output file using imageio_ffmpeg with GPU acceleration
final_video.write_videofile(output_path, codec='libx264', threads=4, preset='fast', ffmpeg_params=['-hwaccel', 'auto'])

print(f"Merged video saved to {output_path}")
