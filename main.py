import time
import video_downloader
import get_video_info
from playwright.sync_api import sync_playwright
import subprocess

# Can configure path here
path = "content"

# Get Video Info
# You're supposed to give the url in the input.
# It is handled in get_video_info.py

with sync_playwright() as playwright:
    video_info = ""
    while not video_info:
        video_info = get_video_info.run(playwright)
        if not video_info:
            time.sleep(1)  # Wait for 1 second before trying again

print(video_info)

# Get m3u8 response
response = video_downloader.send_request(
    video_info["master_url"], video_info["master_headers"])

# Get highest quality url
highest_quality_url = video_downloader.m3u8_parser(response)
print(highest_quality_url)

# Download video
output_file_path = video_downloader.download(highest_quality_url, path,
                          video_info["title"], video_info["master_headers"])
print(output_file_path)

# Move using rclone

# destination_folder = "path/to/destination"
# subprocess.call(['rclone', 'move', output_file_path, destination_folder, '-P'])
