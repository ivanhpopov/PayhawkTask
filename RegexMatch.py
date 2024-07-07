import re

# Define the regex pattern to match IPs
pattern = r"(?<![-\\.\\d])(?:0{0,2}?[0-9]\\.|1\\d?\\d?\\.|2[0-5]?[0-5]?\\.){3}(?:0{0,2}?[0-9]|1\\d?\\d?|2[0-5]?[0-5]?)(?![\\.\\d])"

# Initialize a list to store matched lines
ip_list = []

# Read the lines from the file 
def regex_match(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        
# Iterate over the lines and search for the pattern
def check_file_for_ips():
    for line in lines:
        if re.search(pattern, line, re.IGNORECASE):
            ip_list.append(line.strip())
