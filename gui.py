import tkinter as tk
from tkinter import ttk, Grid
from PIL import Image, ImageTk
from functools import partial
import video_dl

#syntax: Tk(screenName=None, baseName=None, className='Tk', useTk=1)
window = tk.Tk(className=' OctaFX Video Downloader') #where m is the name of the main window object
home_btn, downlaod_btn, settings_btn = None, None, None
home_selected, downloads_selected, settings_selected = True, False, False
video_list, format_list, thumbnail_box = None, None, None

def init_window():
    window.geometry("800x500") #Initial/Default window size
    window.minsize(600, 300)
    photo = tk.PhotoImage(file="flashlogo.png")
    window.iconphoto(False, photo)

    Grid.rowconfigure(window,0,weight=1)
    Grid.columnconfigure(window, 0, weight=1)
    Grid.columnconfigure(window, 1, weight=8)

def menu_on_enter(e):
    e.widget["background"] = "#FEFF9E"

def home_on_leave(e):
    if home_selected is False:
        e.widget["background"] = "black"

def download_on_leave(e):
    if downloads_selected is False:
        e.widget["background"] = "black"

def settings_on_leave(e):
    if settings_selected is False:
        e.widget["background"] = "black"

def left_menu_bar():
    menu_bar = tk.Frame(window, bg="black")
    home_img = Image.open("homebutton.png")
    home_img = home_img.resize((50,50))
    home_icon = ImageTk.PhotoImage(home_img)
    global home_btn
    home_btn = tk.Button(menu_bar,
                         text="Home",
                         fg="green",
                         font=("Times New Roman", "18", "bold"),
                         image=home_icon,
                         compound="top",
                         bg="black",
                         borderwidth=0,
                         command=home_page)
    home_btn.image = home_icon
    #When hover over button
    home_btn.bind('<Enter>', menu_on_enter)
    home_btn.bind('<Leave>', home_on_leave)
    home_btn.grid(row=0, column=0, ipadx=10, ipady=10, sticky="nsew")

    dl_img = Image.open("downloadbuttongreen.png")
    dl_img = dl_img.resize((50,50))
    dl_icon = ImageTk.PhotoImage(dl_img)
    global download_btn
    download_btn = tk.Button(menu_bar,
                         text="Downloads",
                         fg="green",
                         font=("Times New Roman", "18", "bold"),
                         image=dl_icon,
                         compound="top",
                         bg="black",
                         borderwidth=0,
                         highlightcolor="white",
                         command=downloads_page)
    download_btn.image = dl_icon
    download_btn.bind('<Enter>', menu_on_enter)
    download_btn.bind('<Leave>', download_on_leave)
    download_btn.grid(row=1, column=0, ipadx=10, ipady=10, sticky="nsew")
    
    settings_img = Image.open("settings.png")
    settings_img = settings_img.resize((50,50))
    settings_icon = ImageTk.PhotoImage(settings_img)
    global settings_btn
    settings_btn = tk.Button(menu_bar,
                         text="Settings",
                         fg="green",
                         font=("Times New Roman", "22", "bold"),
                         image=settings_icon,
                         compound="top",
                         bg="black",
                         borderwidth=0,
                         highlightcolor="white",
                         command=settings_page)
    settings_btn.image = settings_icon
    settings_btn.bind('<Enter>', menu_on_enter)
    settings_btn.bind('<Leave>', settings_on_leave)
    settings_btn.grid(row=2, column=0, ipadx=10, ipady=10, sticky="nsew")
    
    menu_bar.grid(row=0, column=0, ipady=20, sticky="nsew")
    Grid.rowconfigure(menu_bar,0,weight=1)
    Grid.rowconfigure(menu_bar,1,weight=1)
    Grid.rowconfigure(menu_bar,2,weight=1)
    Grid.columnconfigure(menu_bar, 0, weight=1)

def update_video_list(url):
    

def home_page():
    global home_selected, downloads_selected, settings_selected
    home_btn.config(bg="#FEFF9E")
    download_btn.config(bg="black")
    settings_btn.config(bg="black")
    home_selected = True
    downloads_selected = False
    settings_selected = False
    
    home = tk.Frame(window)
    
    type_link = tk.Frame(home)
    link_input_label = tk.Label(type_link, text="Video link: ", font=("Comic Sans MS", 15))
    input_box = tk.Entry(type_link, font=("Arial", 12))
    input_box.bind("<Return>", lambda event: update_video_list(url=input_box.get()))
    enter_button = tk.Button(type_link, text="Enter", fg="white", font=("Comic Sans MS", "13"), bg="#2F58BF", command=lambda: video_dl.get_video_info(input_box.get()))

    link_input_label.grid(row=0, column=0, ipadx=10, ipady=5, sticky="nsew")
    input_box.grid(row=0, column=1, ipady=5, sticky="ew")
    enter_button.grid(row=0, column=2, padx=20, pady=15, sticky="ew")
    type_link.grid(row=0, column=0, ipadx=20, ipady=15, sticky="nsew")
    Grid.rowconfigure(type_link, 0, weight=1)
    Grid.columnconfigure(type_link, 0, weight=1) #label
    Grid.columnconfigure(type_link, 1, weight=8) #input box
    Grid.columnconfigure(type_link, 2, weight=2) #enter button

    list_row = tk.Frame(home)
    title_label = tk.Label(list_row, text="Video: ", font=("Arial", 13, "bold"))
    format_label = tk.Label(list_row, text="Available download formats: ", font=("Arial", 13, "bold"))
    thumbnail_label = tk.Label(list_row, text="Thumbnail: ", font=("Arial", 13, "bold"))
    title_label.grid(row=0, column=0, sticky="nse")
    format_label.grid(row=0, column=1, sticky="nse")
    thumbnail_label.grid(row=0, column=2, sticky="nse")

    
    list_row.grid(row=1, column=0, ipadx=20, ipady=15, sticky="nsew")
    Grid.rowconfigure(list_row, 0, weight=1) #for list box titles
    Grid.rowconfigure(list_row, 1, weight=8) #for listboxes
    Grid.columnconfigure(list_row, 0, weight=1) #for video list(multiple videos if the link is a youtube playlist link)
    Grid.columnconfigure(list_row, 1, weight=1) #for available format list
    Grid.columnconfigure(list_row, 2, weight=1) #for video thumbnail
    
    home.grid(row=0, column=1, padx=10, pady=10, ipadx=20, ipady=20, sticky="nsew")
    Grid.columnconfigure(home, 0, weight=1)
    Grid.rowconfigure(home, 0, weight=1) #for type_link
    Grid.rowconfigure(home, 1, weight=4) #for download options and thumbnail
    Grid.rowconfigure(home, 2, weight=3) #for video details and download button

def downloads_page():
    global home_selected, downloads_selected, settings_selected
    home_btn.config(bg="black")
    download_btn.config(bg="#FEFF9E")
    settings_btn.config(bg="black")
    home_selected = False
    downloads_selected = True
    settings_selected = False

def settings_page():
    global home_selected, downloads_selected, settings_selected
    home_btn.config(bg="black")
    download_btn.config(bg="black")
    settings_btn.config(bg="#FEFF9E")
    home_selected = False
    downloads_selected = False
    settings_selected = True

def main():
    init_window()
    left_menu_bar()
    home_page()

main()

