import re

# opening and reading the file

# declaring the regex pattern for IP addresses 
pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')  
# initializing the list object 
lst=[] 

file_path='/home/calaroshi/PayhawkTask/extractips/myfile.txt'
# extracting the IP addresses 
def check_file_for_ips(file_path):
    with open(file_path) as fh: 
        fstring = fh.readlines()
    for line in fstring: 
        line = line.rstrip()
        result = (pattern.match(line))
        if result:
            result=result.group()
            lst.append(result)

check_file_for_ips(file_path)
print(lst)

# displaying the extracted IP addresses 
#print(lst)