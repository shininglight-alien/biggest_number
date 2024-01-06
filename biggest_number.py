# Ask user to input 3 numbers. Find and print the biggest number using only if-else statement.

# pseudocode

import tkinter as tk
from tkinter import PhotoImage

# setup
root = tk.Tk()
root.title("What's the Biggest Number?")

# set window size to full screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")