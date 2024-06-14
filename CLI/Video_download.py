"""
Developed by Hareeshwar N K
"""
from pytube import YouTube
def check_link(url):
    """Checks if the provided YouTube URL is valid."""
    try:
        YouTube(url).check_availability()
        return True
    except Exception:
        return False

def get_video_stream(yt, resolution):

    """Retrieves the video stream based on the desired resolution."""

    if resolution == "lowest":
        return yt.streams.get_lowest_resolution()
    elif resolution == "highest":
        return yt.streams.get_highest_resolution()
    else:
        try:
            video = yt.streams.get_by_resolution(resolution)
            if video is None: raise Exception
            return video
        except Exception:
            print(f"The given quality '{resolution}' is not available.")
            return get_available_resolutions(yt)

def get_available_resolutions(yt):
    """Displays available resolutions and prompts the user for selection."""
    print("\n Available resolutions:")
    for stream in yt.streams.filter(progressive=True):
        print(f"id: {stream.itag} - {stream.resolution}")

    quality = input("Enter the desired quality or id: ")
    
    try:
        video = yt.streams.filter(progressive=True, resolution=quality).first()
        if video is None: raise Exception
        return video
    
    except Exception:
        try:
            video = yt.streams.get_by_itag(quality)
            if video is None: raise Exception
            return video
        except Exception:
            print("Invalid selection.")
            return None

def video_download(url, path="", resolution="highest",yestoall=False):

    """
    Downloads the YouTube video with optional path and resolution selection.

    Args:
        url (str): The URL of the YouTube video.
        path (str, optional): The path to save the downloaded video. Defaults to the current directory.
        resolution (str, optional): The desired resolution (lowest, highest, or "720p", "480p", "360p", "240p", "144p"). Defaults to "highest".
        yestoall(bool,optional): When True is passed, Doesn't wait for user confirmation. Default value False
    Returns:
        str: A success message with the download path or an error message.
    """

    if not check_link(url):
        return "Link is invalid. or Check Internet Connection..."

    try:
        yt = YouTube(url)
        video_title = yt.title

        # Get video stream 
        video = get_video_stream(yt, resolution)

        if video is None:
            return "No valid resolution found."

        print(f"The file size of video '{video_title}' is about {video.filesize_mb} MB")

        if yestoall:
            print("The Video is Downloading... \n Please Wait :) ")
            if path:
                download_path = video.download(output_path=path)
                return f"Successfully downloaded to {download_path}"
            else:
                download_path = video.download()
                return f"Successfully downloaded to {download_path}"
            
        if input("Do you want to continue? (y/n): ").lower() == "y":
            print("The Video is Downloading... \n Please Wait :) ")
            if path:
                download_path = video.download(output_path=path)
                return f"Successfully downloaded to {download_path}"
            else:
                download_path = video.download()
                return f"Successfully downloaded to {download_path}"
        else:
            print("Operation cancelled!")
            return "Cancelled"

    except Exception as e:
        print(f"Error occurred: {e}")
        return f"Download failed: {e}"

#Used for Running this module as Main program
if __name__ == "__main__":
    
    url = input("Enter YouTube URL: ")
    output_path = input("Enter path (or leave blank for current directory): ")
    resolution = input("Enter desired resolution (lowest/highest/resolution_value): ").lower()
    if resolution:
        result = video_download(url, output_path, resolution)
    else:
        result = video_download(url,output_path)    
    print(result)
