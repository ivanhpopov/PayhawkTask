import re

# opening and reading the file
with open('/home/ipopov/PayhawkTask/extractips/myfile.txt') as fh: 
   fstring = fh.readlines()

# declaring the regex pattern for IP addresses 
pattern = re.compile(r'(?<![-\\.\\d])(?:0{0,2}?[0-9]\\.|1\\d?\\d?\\.|2[0-5]?[0-5]?\\.){3}(?:0{0,2}?[0-9]|1\\d?\\d?|2[0-5]?[0-5]?)(?![\\.\\d])') 
  
# initializing the list object 
lst=[] 
  
# extracting the IP addresses 
def check_ip_add():
    for line in fstring: 
        line = line.rstrip()
        result = pattern.search(line) 
        if result:
            lst.append(line)

check_ip_add()
# displaying the extracted IP addresses 
print(lst) 
