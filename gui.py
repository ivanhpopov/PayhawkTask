import tkinter as tk
from tkinter import filedialog

def open_text_file():
    # Ask the user to select a text file
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])

    if file_path:
        # Read the content of the selected file
        with open(file_path, "r") as file:
            content = file.read()
            
        # Create a new window to display the content
        window = tk.Toplevel(root)
        window.title(f"Content of {file_path}")
        text_widget = tk.Text(window, wrap=tk.WORD)
        text_widget.insert("1.0", content)
        text_widget.pack()

# Create the main window
root = tk.Tk()
root.title("IP address checker")
root.geometry("500x390")

# Create a button to open the text file
open_button = tk.Button(root, text="Open Text File", command=open_text_file)
open_button.pack()

#Label for first field
label_single = tk.Label(root, text = "Check one IP here:")
label_single.pack()

#Text field to paste single IP
Single_addr = tk.Text(root, height=2, width=52)
Single_addr.pack()

#Label for second field
label_multi = tk.Label(root, text = "Your IPs from opened file:")
label_multi.pack()

#Text field for multiple IPs
Multiple_addr = tk.Text(root, height=14, width=52)
Multiple_addr.pack()

#Button to run the check against VirusTotal API
run1_button = tk.Button(root, text="Single", command=open_text_file)
run1_button.pack(side="left")

run2_button = tk.Button(root, text="Exit", command=root.destroy)
run2_button.pack(side="right")

run3_button = tk.Button(root, text="Bulk", command=root.destroy)
run3_button.place(anchor="se")
run3_button.pack()
# Run the Tkinter event loop
root.mainloop()