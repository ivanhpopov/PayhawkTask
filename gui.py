import tkinter as tk
from tkinter import filedialog
from API import check_ip_on_virustotal
#from RegexMatch import check_file_for_ips
import re

pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
lst=[]
multiple_test=[]
API_key = '656eb69d98741d422816b890c809f1d8ac78ff4ac5e225a0048ad11cfdb9bd06'

def check_file_for_ips(file_path):
    with open(file_path) as fh: 
        fstring = fh.readlines()
    for line in fstring: 
        line = line.rstrip()
        result = (pattern.match(line))
        if result:
            result=result.group()
            lst.append(result)

def get_input_single():
    input_text_single = Single_addr.get("1.0",'end-1c')
    result = check_ip_on_virustotal(input_text_single, API_key)
    return result
    
def get_input_multiple():
    input_text_multiple = Multiple_addr.get()
    
def popup_bonus_multiple():
    win = tk.Toplevel()
    win.geometry("380x150")
    win.wm_title("Multiple IP check")
    for ip in lst:
        multiple_test.append(check_ip_on_virustotal(ip, API_key) + "\n")
    label = tk.Label(win, text=multiple_test)
    label.grid(row=2, column=2)

def popup_bonus_single():
    win = tk.Toplevel()
    win.geometry("380x150")
    win.wm_title("Single IP check")
    label = tk.Label(win, text=get_input_single())
    label.grid(row=2, column=2)


def open_text_file():
    # Ask the user to select a text file
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
            with open(file_path, "r") as file:
                 Multiple_addr.delete("1.0", tk.END)
                 Multiple_addr.insert(tk.END, file.read())
                 check_file_for_ips(file_path)

def output_ips_to_field():
    Multiple_addr.delete("1.0", tk.END)
    for i in lst:
        Multiple_addr.insert(tk.END, i)


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
run1_button = tk.Button(root, text="Single", command=popup_bonus_single)
run1_button.pack(side="left")

run2_button = tk.Button(root, text="Exit", command=root.destroy)
run2_button.pack(side="right")

run3_button = tk.Button(root, text="Bulk", command=popup_bonus_multiple)
run3_button.place(anchor="se")
run3_button.pack()
# Run the Tkinter event loop
root.mainloop()