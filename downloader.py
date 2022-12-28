from pytube import YouTube, exceptions
from pytube.cli import on_progress

try:
    link = input("Youtube link: ")
    yt = YouTube(link, on_progress_callback=on_progress)
except exceptions.RegexMatchError:
    print("Please supply a valid Youtube link.")
else:
    print("Title: ", yt.title)
    print("Views: ", yt.views)

    print("Downloading...")

    yd = yt.streams.get_highest_resolution()
    yd.download()

    print("Done!")
