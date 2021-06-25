import tkinter

#syntax: Tk(screenName=None, baseName=None, className='Tk', useTk=1)
window = tkinter.Tk(className=' OctaFX Video Downloader') #where m is the name of the main window object

window.geometry("500x200") #Initial/Default window size
photo = tkinter.PhotoImage(file="flashlogo.png")
window.iconphoto(False, photo)

greeting = tkinter.Label(text="Hello, Tkinter")
greeting.pack()

window.mainloop()
