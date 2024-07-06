import re

# Read the lines from the file (assuming the file is named "myfile.txt")
with open('/home/ipopov/PayhawkTask/extractips/myfile.txt', 'r') as file:
    lines = file.readlines()

# Define the regex pattern to match whole words (e.g., "Foo")
pattern = r"(?<![-\\.\\d])(?:0{0,2}?[0-9]\\.|1\\d?\\d?\\.|2[0-5]?[0-5]?\\.){3}(?:0{0,2}?[0-9]|1\\d?\\d?|2[0-5]?[0-5]?)(?![\\.\\d])"

# Initialize a list to store matched lines
ip_list = []

# Iterate over the lines and search for the pattern
def check_file_for_ips():
    for line in lines:
        if re.search(pattern, line, re.IGNORECASE):
            ip_list.append(line.strip())

print (ip_list)