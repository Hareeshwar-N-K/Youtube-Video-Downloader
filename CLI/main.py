from Video_download import video_download
value = False
try:
    with open("links.txt",'r') as file:
        if "##" in file.readline():raise Exception("Update link.txt file if its there")
        links = file.readlines()
        file.close()

    resolution = input("Type the resolution for all the videos(lowest/highest/resolution_value): ").lower()
    output_path = input("Enter the output folder location:")
    choice = input("Want to be notified for each download?(y/n):").lower()
    if choice == 'n': value = True
    for each_Link in links:
         video_download(each_Link,output_path,resolution,value)
except Exception as e:
    print("Please Check where links.txt file exists!")
    print(e)        
