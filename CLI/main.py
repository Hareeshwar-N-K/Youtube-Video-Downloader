from Video_download import video_download

with open("links.txt",'r') as file:

    links = file.readlines()
    file.close()

for each_Link in links:
     video_download(each_Link,"D:\Programming\Projects_Hari\Automatic Youtube Video Downloader in Python\outputs","lowest",True)

