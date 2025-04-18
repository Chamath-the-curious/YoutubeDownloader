
import yt_dlp
import os
import sys

if getattr(sys, 'frozen', False): # running .exe
    base_path = sys._MEIPASS
else:
    base_path = os.path.dirname(__file__) # running python script

#bundled ffmpeg and ffprobe
ffmpeg_path = os.path.join(base_path, "ffmpeg")

print('*' * 40)
print('*' + ' ' * 10 + 'Youtube Downloader' + ' ' * 10 + '*')


def help():
    print('*' * 40)
    print("* [1] Download video (MP4)" + ' ' * 13 + '*')
    print("* [2] Download audio (MP3)" + ' ' * 13 + '*')
    print("* [3] Download playlist (MP4)" + ' ' * 10 + '*')
    print("* [4] Download playlist (MP3)" + ' ' * 10 + '*')
    print("* [0] exit" + ' ' * 29 + '*')
    print('*' * 40 + '\n')

def download_res(url: str, ydl_opt: dict):
    with yt_dlp.YoutubeDL(ydl_opt) as ydl:
        ydl.download([url])
       
help()

while True:

    command = input("Enter command: ")

    if command == '0':
        print("Thanks for using Youtube Downloader!")
        print("An open source project by ChamaththeCurious")
        input("Press Enter to exit...")
        break


    if command == '1':

        url = input("Enter youtube url: ")

        print("\nChoose video quality:")
        print("[1] 1080p")
        print("[2] 720p")
        print("[3] 480p")
        print("[4] Best available\n")

        quality_map = {
            '1': '137', #1080p
            '2': '136', #720p
            '3': '135', #480p
            '4': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best'
        }

        while True:
            quality = input("Enter quality: ")
            if quality in quality_map:
                break

        with yt_dlp.YoutubeDL({'ffmpeg_location': ffmpeg_path}) as ydl:
            info = ydl.extract_info(url, download=False)
            formats = info.get('formats', [])

        avail_qualities = [format['format_id'] for format in formats]

        if quality_map[quality] not in avail_qualities:
            quality = '4'
            print("\nThe quality you selected is not available for this video.")
            print("Downloading best quality possible\n")

        if quality != '4':
            format_value = quality_map[quality]
            ydl_format = f"{format_value}+bestaudio[ext=m4a]"
        else:
            ydl_format = quality_map['4']

        ydl_opts = {
            'format': ydl_format,
            'outtmpl': '%(title)s.%(ext)s',
            'merge_output_format': 'mp4',
            'ffmpeg_location': ffmpeg_path,  
        }

        try:
            download_res(url, ydl_opts)
            print("Download successful!")
        except Exception as e:
            print(f"Error :{e}")

    if command == '2':

        url = input("Enter youtube url: ")

        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': '%(title)s.%(ext)s',  
            'postprocessors': [
                {
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }
            ],
            'ffmpeg_location': ffmpeg_path
        }
        
        try:
            download_res(url, ydl_opts)
            print("Download successful!")
        except Exception as e:
            print(f"Error :{e}")

    if command == '3':

        print("Make sure your playlist is set to public before downloading.")
        url = input("Enter playlist url: ")

        ydl_opts = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=4]/best',
            'outtmpl': '%(playlist_title)s/%(playlist_index)s - %(title)s.%(ext)s',
            'merge_output_format': 'mp4',
            'ffmpeg_location': ffmpeg_path
        }

        try:
            download_res(url, ydl_opts)
            print("Download successful!")
        except Exception as e:
            print(f"Error :{e}")

    if command == '4':

        print("Make sure your playlist is set to public before downloading.")
        url = input("Enter playlist url: ")

        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': '%(playlist_title)s/%(playlist_index)s - %(title)s.%(ext)s',  
            'postprocessors': [
                {
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }
            ],
            'ffmpeg_location': ffmpeg_path
        }

        try:
            download_res(url, ydl_opts)
            print("Download successful!")
        except Exception as e:
            print(f"Error: {e}")

    else:
        print("Please enter a valid command from the menu\n")
        help()