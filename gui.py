import tkinter as tk
from tkinter import messagebox

# Create the main application window
root = tk.Tk()
root.title("IP Inspection tool")

def get_ips_from_file(filename):
    with open(filename, 'r') as f:
        ips = f.read()
    return ips
# Function to handle Option 1
def option1():
    print("Option 1 selected")
    messagebox.showinfo("Option 1", "Option 1 selected")

# Function to handle Option 2
def option2():
    print("Option 2 selected")
    messagebox.showinfo("Option 2", "Option 2 selected")

# Create buttons for the options
button1 = tk.Button(root, text="Option 1", command=option1)
button1.pack()

button2 = tk.Button(root, text="Option 2", command=option2)
button2.pack()

# Start the main event loop
root.mainloop()