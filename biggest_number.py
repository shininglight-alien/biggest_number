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

# create a frame to hold the widgets
frame = tk.Frame(root)
frame.pack()

# create three labels for the numbers
label1 = tk.Label(frame, text="First Number: ")
label2 = tk.Label(frame, text="Second Number: ")
label3 = tk.Label(frame, text="Third Number: ")

# create three entry widgets for the numbers
entry1 = tk.Entry(frame)
entry2 = tk.Entry(frame)
entry3 = tk.Entry(frame)
