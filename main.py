from yt_dlp import YoutubeDL

URLS = [input('Enter video: ')]
with YoutubeDL() as ydl:
    ydl.download(URLS)
