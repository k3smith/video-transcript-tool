#from pytube import YouTube
 
from pytubefix import YouTube
from pytubefix.cli import on_progress
 
 
def download_video(url, output_path):
    try:
        yt = YouTube(url, on_progress_callback = on_progress)
        stream = yt.streams.get_highest_resolution()
        print("Downloading:", yt.title)
        stream.download(output_path)
        print("Download completed successfully!")
    except Exception as e:
        print("Error:", str(e))
 
def download_videos_from_file(file_path, output_path):
    with open(file_path, 'r') as file:
        urls = file.readlines()
        for url in urls:
            url = url.strip()  # Remove leading/trailing whitespaces
            download_video(url, output_path)
 
if __name__ == "__main__":
    input_type = input("Enter '1' if you want to input a single URL, '2' if you want to provide a file containing URLs: ")
   
    if input_type == '1':
        video_url = input("Enter the URL of the YouTube video: ")
        download_video(video_url, 'videos')
    elif input_type == '2':
        file_path = input("Enter the path to the file containing URLs: ")
        download_videos_from_file(file_path, 'videos')
    else:
        print("Invalid input. Please enter '1' or '2'.")