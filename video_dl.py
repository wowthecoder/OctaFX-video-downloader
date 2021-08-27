import youtube_dl
from tkinter import messagebox

ytdl = youtube_dl.YoutubeDL()

def get_video_info(url):
    print(url)
    try:
        video_data = ytdl.extract_info(url, download=False)
        print(video_data)
    except Exception as e:
        print(e)
        messagebox.showerror("Invalid link", "Invalid video link provided, could not download video")
        
def     
        

    

