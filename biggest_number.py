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

# background image
background_image = PhotoImage(file=r"C:\Users\Ellaine\Downloads\The Quest for Biggest Number.png")
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

# create a frame to hold the widgets
frame = tk.Frame(root)
frame.place(relx=0.5, rely=0.58, anchor="center")

# create three subframes for each number
frame1 = tk.Frame(frame, borderwidth=10, relief="groove", bg="light blue")
frame2 = tk.Frame(frame, borderwidth=10, relief="groove", bg="light blue")
frame3 = tk.Frame(frame, borderwidth=10, relief="groove", bg="light blue")

# create three labels for the numbers
label1 = tk.Label(frame1, text="First Number: ", width=20, height=3, font=("Comic Sans MS Bold", 15), fg="dark blue")
label2 = tk.Label(frame2, text="Second Number: ", width=20, height=3, font=("Comic Sans MS Bold", 15), fg="dark blue")
label3 = tk.Label(frame3, text="Third Number: ", width=20, height=3, font=("Comic Sans MS Bold", 15), fg="dark blue")

# create three entry widgets for the numbers
entry1 = tk.Entry(frame1, font=("Comic Sans MS Bold", 15), fg="blue", justify="center")
entry2 = tk.Entry(frame2, font=("Comic Sans MS Bold", 15), fg="blue", justify="center")
entry3 = tk.Entry(frame3, font=("Comic Sans MS Bold", 15), fg="blue", justify="center")

# create a label for the result
result = tk.Label(frame, text="Biggest Number: ")

# define a function to find and display the biggest number
def find_biggest():
    # Get the numbers from the entries
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    num3 = float(entry3.get())

    # find the biggest number using only if-else statement
    if num1 >= num2 and num1 >= num3:
        biggest = num1
    elif num2 >= num1 and num2 >= num3:
        biggest = num2
    else:
        biggest = num3

    # display the result
    result.config(text="GIGANTOSAURUS NUMERALUS: " + str(biggest))

# create a button to trigger the function
button = tk.Button(frame, text="Find Now!", command=find_biggest, width=20, height=1, font=("Comic Sans MS Bold", 15), bg="light blue")

# arrange the widgets using grid layout
frame1.grid(row=0, column=0, padx=50, pady=20)
frame2.grid(row=0, column=1, padx=50, pady=20)
frame3.grid(row=0, column=2, padx=50, pady=20)

# create a label for the result
result = tk.Label(frame, text="GIGANTOSAURUS NUMERALUS: ", font=("Comic Sans MS Bold", 15), padx=50, pady=30, fg="dark blue")

label1.pack(side="top")
entry1.pack(anchor="center")

label2.pack(side="top")
entry2.pack(anchor="center")

label3.pack(side="top")
entry3.pack(anchor="center")

button.grid(row=1, column=0, columnspan=3)
result.grid(row=2, column=0, columnspan=3)

# define a function to center the window on the screen
def center_window():
    # Update the window's geometry
    root.update_idletasks()
    # Get the window's width and height
    window_width = root.winfo_width()
    window_height = root.winfo_height()
    # Get the screen's width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    # Calculate the position of the window
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    # Set the window's geometry
    root.geometry(f"+{x}+{y}")

# call the function to center the window
center_window()

# start the main loop
root.mainloop()