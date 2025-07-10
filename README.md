# YoutubeDownloader
A standalone command-line utility for downloading YouTube videos (MP4) and audio (MP3), including playlist support, with bundled FFmpeg/ffprobe.

## About this project

There are a lot of websites/scripts to download YouTube videos or convert videos to MP3 files, but most of them don't work or are full of ads, making them unusable, so I created this as my first ever coding project.

**This project was built using the following tools and technologies:**

- ![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white)
- ![yt-dlp](https://img.shields.io/badge/yt--dlp-latest-yellow?logo=youtube&logoColor=white)
- ![FFmpeg](https://img.shields.io/badge/FFmpeg-4.x-green?logo=ffmpeg&logoColor=white)
- ![PyInstaller](https://img.shields.io/badge/PyInstaller-bundler-lightgrey?logo=windows&logoColor=white)

## Features

* Download video (MP4) in selectable qualities (1080p, 720p, 480p, or best available)

* Download audio (MP3) with automatic conversion

* Download public playlists (MP4 or MP3) into organized folders

* Bundled FFmpeg/ffprobe, no external dependencies

* Single-file executable,no Python install required

## Installation 

1. Create a new folder on your computer
2. Download `Youtubedownloader.exe` from Releases to that folder 

## Usage

Run `Youtubedownloader.exe`

Follow the interactive menu:
```scss
[1] Download video (MP4)
[2] Download audio (MP3)
[3] Download playlist (MP4)
[4] Download playlist (MP3)
[0] Exit
```

 - For video, choose your desired quality (IF the desired quality is not available it will download the best quality possible)
 - For playlist, ensure they are public.

All downloads appear in the folder the .exe file is in (or playlist subfolder for playlists).

**If you want to run and edit `Youtubedownloader.py`**

 1. Clone the repo:

```bash
git clone https://github.com/Chamath-the-curious/YoutubeDownloader.git
```
 2. Install dependencies

```bash
pip install yt-dlp
```
 3. Download and setup ffmpeg and ffprobe

 Download `ffprobe.exe` and `ffmpeg.exe` from releases. Copy these into a file named `ffmpeg` next to `Youtubedownloader.exe` (These two should be in same directory)

 Run the python script

 **or**

 4. Build the EXE with bundled FFmpeg:

```bash
pip install pyinstaller
pyinstaller --onefile --console --add-data "ffmpeg;ffmpeg" Youtubedownloader.py
```
use : instead of ; if you are on linux

## Known Errors

- Sign in to confirm you are not a bot - if you are getting this error make sure are signed into youtube in your web browser.

  Still getting this error? yt-dlp package need to collect cookies from your browser, most likely you are not using supported browser which are Chrome, Edge, Chromium, Opera or Firefox. 

## License

Distributed under MIT license. See `LICENSE.txt` for more information.

## Contact

Chamath Sasmitha - [sasmithachamath@gmail.com](mailto:sasmithachamath@gmail.com)

