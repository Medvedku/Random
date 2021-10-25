import tkinter as tk
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile
import tkinter.scrolledtext
import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack
from scipy.io import wavfile
import pandas as pd
import wave, struct

#colours
C_RUBY_RED = "#A4161A"

root = tk.Tk()

canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)

#logo
logo = Image.open("logo.png")
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

#instruction
instruction = tk.Label(root, text="Select .WAV file", font="Courier")
instruction.grid(columnspan=3, column=0, row=1)

def open_file():
    browse_text.set("loading...")
    file = askopenfile(parent=root, mode="rb", title="Chose a file", filetype=[("WAVko", "*.WAV")])
    if file:
        samrate, data = wavfile.read(file)
        browse_text.set("Cool")
        msg = "File with samplerate of {} Hz and {} channels.".format( samrate, len(data[1]))
        instruction.config(text=msg)
        #text box
        text_box = tk.scrolledtext.ScrolledText(root, height=10, width=30, padx=15, pady=15)
        for i in data[:100]:
            text_box.insert(1.0, str(i)+"\n")
        text_box.tag_configure("center", justify="center")
        text_box.tag_add("center", 1.0, "end")

        text_box.grid(column=1, row=3)
        browse_text.set("Browse")
    else:
        browse_text.set("Browse")

#browse buttons_frame
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text, font=("Courier",16),
                        bg=C_RUBY_RED, borderwidth=2, fg="white",
                        height=2, width=15, command=lambda:open_file() )
browse_text.set("Browse")
browse_btn.grid(column=1, row=2)

canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)


root.mainloop()
