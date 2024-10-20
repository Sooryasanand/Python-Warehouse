import tkinter as tk
from tkinter import ttk

from PIL import Image as PImage
from PIL import ImageTk

python_blue = "#168FC1"
python_blue_inactive = "#216583"
width_ = 600
image_height = 150


def disable(root, text, callback=None):
    return tk.Button(root, text=text, command=callback, background=python_blue_inactive, padx=0, relief=tk.FLAT, font="Arial 11 bold", foreground="white")


def Toplevel(title):
    tl = tk.Toplevel(width=width_)
    tl.resizable(False, False)
    tl.title(title)
    #tl.protocol("WM_DELETE_WINDOW", disable)
    return tl


def Button(root, text, callback=None):
    return tk.Button(root, text=text, command=callback, background=python_blue, padx=0, relief=tk.FLAT, font="Arial 11 bold", foreground="white")


def Frame(root):
    return tk.Frame(root, width=width_)


def Label(root, text):
    return tk.Label(root, text=text, font="Helvetica 12 bold", foreground=python_blue)


def Entry(root):
    return tk.Entry(root, font="Helvetica 12 bold", foreground=python_blue, show=None)


def Separator(root):
    return ttk.Separator(root, orient='horizontal')


# Dont use this for the icon image
def Image(root, path):
    img = ImageTk.PhotoImage(PImage.open(path).resize((width_, image_height)))
    lbl = tk.Label(root, image=img)
    lbl.photo = img
    return lbl

def WinIcon(self, path):
    icon_img = ImageTk.PhotoImage(PImage.open(path))
    self.root.wm_iconphoto(False, icon_img)