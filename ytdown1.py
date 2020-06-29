from pytube import YouTube
print("Welcome in Youtube video downloader.")
link =input("Enter link: ")

vid = YouTube(link)

videos = vid.streams.filter(file_extension='mp4').all()
i=1
for qlt in videos:
    print(str(i)+" :"+str(qlt))
    print(" ")
    i +=1

qlt_num = int(input("Enter number: "))

video = videos[qlt_num-1]
video.download()
print("Downloaded")

