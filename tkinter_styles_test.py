import tkinter as tk
from tkinter import ttk

class StyleDemo(tk.Tk):
    def __init__(self):
        super().__init__()

        #root window
        self.title('Theme Demo')
        self.geometry('400x300')
        self.style = ttk.Style(self)

        #Label
        label = ttk.Label(self, text="Name:")
        label.grid(column=0, row=0, padx=10, pady=10, sticky="w")
        #entry
        textbox = ttk.Entry(self)
        textbox.grid(column=1, row=0, padx=10, pady=10, sticky="w")
        #button
        btn = ttk.Button(self, text="Show", command=lambda: self.style.theme_use(textbox.get()))
        btn.grid(column=2, row=0, padx=10, pady=10, sticky="w")

        #radio button
        self.selected_theme = tk.StringVar()
        theme_frame = ttk.LabelFrame(self, text="Themes")
        theme_frame.grid(padx=10, pady=10, ipadx=20, ipady=20, sticky="w")

        for theme_name in self.style.theme_names():
            radioBtn = ttk.Radiobutton(
                theme_frame,
                text=theme_name,
                value=theme_name,
                variable=self.selected_theme,
                command=self.change_theme)
            radioBtn.pack(expand=True, fill="both")

    def change_theme(self):
        self.style.theme_use(self.selected_theme.get())

app = StyleDemo()
