import yt_dlp
import os
import sys
from colorama import init, Fore, Back, Style

# Initialize colorama
init(autoreset=True)

# Color definitions for better readability
TITLE_COLOR = Fore.CYAN + Style.BRIGHT
MENU_COLOR = Fore.GREEN
INPUT_COLOR = Fore.YELLOW
SUCCESS_COLOR = Fore.GREEN + Style.BRIGHT
ERROR_COLOR = Fore.RED + Style.BRIGHT
INFO_COLOR = Fore.BLUE + Style.BRIGHT
BORDER_COLOR = Fore.MAGENTA

def print_banner():
    print('\n' + BORDER_COLOR + '*' * 40)
    print(BORDER_COLOR + '*' + TITLE_COLOR + ' ' * 10 + 'Youtube Downloader' + ' ' * 10 + BORDER_COLOR + '*')
    print(BORDER_COLOR + '*' * 40 + '\n')

def help():
    print(BORDER_COLOR + '*' * 40)
    print(BORDER_COLOR + "* " + MENU_COLOR + "[1] Download video (MP4)" + ' ' * 13 + BORDER_COLOR + '*')
    print(BORDER_COLOR + "* " + MENU_COLOR + "[2] Download audio (MP3)" + ' ' * 13 + BORDER_COLOR + '*')
    print(BORDER_COLOR + "* " + MENU_COLOR + "[3] Download playlist (MP4)" + ' ' * 10 + BORDER_COLOR + '*')
    print(BORDER_COLOR + "* " + MENU_COLOR + "[4] Download playlist (MP3)" + ' ' * 10 + BORDER_COLOR + '*')
    print(BORDER_COLOR + "* " + MENU_COLOR + "[0] Exit" + ' ' * 29 + BORDER_COLOR + '*')
    print(BORDER_COLOR + '*' * 40 + '\n')

def print_exit_message():
    print(INFO_COLOR + "\nThanks for using Youtube Downloader!")
    print(INFO_COLOR + "An open source project by ChamaththeCurious")
    input(INPUT_COLOR + "\nPress Enter to exit...")

def download_res(url: str, ydl_opt: dict):
    # Add geo-bypass for restricted content
    common_opts = {
        'geo_bypass_country': 'US',
        'geo_bypass': True
    }
    # Merge common options with specific options
    ydl_opt.update(common_opts)
    with yt_dlp.YoutubeDL(ydl_opt) as ydl:
        print(INFO_COLOR + "\nStarting download...")
        ydl.download([url])
        print(SUCCESS_COLOR + "\nDownload completed successfully!")
        print(INFO_COLOR + "\nReturning to main menu...")
        print("\n" + BORDER_COLOR + "="*40)
        help()

def main():
    print_banner()
    help()

    while True:
        try:
            command = input(INPUT_COLOR + "\nEnter command: ")

            if command == '0':
                print_exit_message()
                sys.exit(0)

            elif command == '1':
                url = input(INPUT_COLOR + "\nEnter youtube url: ")

                print(INFO_COLOR + "\nChoose video quality:")
                print(MENU_COLOR + "[1] 8K (4320p)")
                print(MENU_COLOR + "[2] 4K (2160p)")
                print(MENU_COLOR + "[3] 1080p")
                print(MENU_COLOR + "[4] 720p")
                print(MENU_COLOR + "[5] 480p")
                print(MENU_COLOR + "[6] Best available\n")

                quality_map = {
                    '1': '571', #8K
                    '2': '313', #4K
                    '3': '137', #1080p
                    '4': '136', #720p
                    '5': '135', #480p
                    '6': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best'
                }

                while True:
                    quality = input(INPUT_COLOR + "Enter quality: ")
                    if quality in quality_map:
                        break
                    print(ERROR_COLOR + "\nInvalid quality selection. Please try again.")

                with yt_dlp.YoutubeDL() as ydl:
                    try:
                        print(INFO_COLOR + "\nChecking video availability...")
                        info = ydl.extract_info(url, download=False)
                        formats = info.get('formats', [])
                        avail_qualities = [format['format_id'] for format in formats]

                        if quality != '6' and quality_map[quality] not in avail_qualities:
                            print(ERROR_COLOR + "\nThe selected quality is not available for this video.")
                            print(INFO_COLOR + "Switching to best available quality...\n")
                            quality = '6'

                        if quality != '6':
                            format_value = quality_map[quality]
                            ydl_format = f"{format_value}+bestaudio[ext=m4a]"
                        else:
                            ydl_format = quality_map['6']

                        ydl_opts = {
                            'format': ydl_format,
                            'outtmpl': '%(title)s.%(ext)s',
                            'merge_output_format': 'mp4'
                        }

                        download_res(url, ydl_opts)
                    except Exception as e:
                        print(ERROR_COLOR + f"\nError: {str(e)}")
                        print(INFO_COLOR + "\nReturning to main menu...")
                        print("\n" + BORDER_COLOR + "="*40)
                        help()

            elif command == '2':
                url = input(INPUT_COLOR + "\nEnter youtube url: ")

                ydl_opts = {
                    'format': 'bestaudio/best',
                    'outtmpl': '%(title)s.%(ext)s',  
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192',
                    }]
                }
                
                try:
                    download_res(url, ydl_opts)
                except Exception as e:
                    print(ERROR_COLOR + f"\nError: {str(e)}")
                    print(INFO_COLOR + "\nReturning to main menu...")
                    print("\n" + BORDER_COLOR + "="*40)
                    help()

            elif command == '3':
                print(INFO_COLOR + "\nMake sure your playlist is set to public before downloading.")
                url = input(INPUT_COLOR + "Enter playlist url: ")

                ydl_opts = {
                    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
                    'outtmpl': '%(playlist_title)s/%(playlist_index)s - %(title)s.%(ext)s',
                    'merge_output_format': 'mp4'
                }

                try:
                    download_res(url, ydl_opts)
                except Exception as e:
                    print(ERROR_COLOR + f"\nError: {str(e)}")
                    print(INFO_COLOR + "\nReturning to main menu...")
                    print("\n" + BORDER_COLOR + "="*40)
                    help()

            elif command == '4':
                print(INFO_COLOR + "\nMake sure your playlist is set to public before downloading.")
                url = input(INPUT_COLOR + "Enter playlist url: ")

                ydl_opts = {
                    'format': 'bestaudio/best',
                    'outtmpl': '%(playlist_title)s/%(playlist_index)s - %(title)s.%(ext)s',  
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192',
                    }]
                }

                try:
                    download_res(url, ydl_opts)
                except Exception as e:
                    print(ERROR_COLOR + f"\nError: {str(e)}")
                    print(INFO_COLOR + "\nReturning to main menu...")
                    print("\n" + BORDER_COLOR + "="*40)
                    help()

            else:
                print(ERROR_COLOR + "\nInvalid command!")
                help()

        except KeyboardInterrupt:
            print(ERROR_COLOR + "\n\nProgram interrupted by user.")
            print_exit_message()
            sys.exit(0)
        except Exception as e:
            print(ERROR_COLOR + f"\nUnexpected error: {str(e)}")
            print(INFO_COLOR + "\nReturning to main menu...")
            print("\n" + BORDER_COLOR + "="*40)
            help()

if __name__ == "__main__":
    main()
