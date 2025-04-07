from pytube import YouTube

link = input("Enter YouTube URL: ").strip()
yt = YouTube(link)

print("Title: ", yt.title)
print("Views: ", yt.views)

yd = yt.streams.get_highest_resolution()
yd.download('./downloadedVideos')

print("Download Complete!")