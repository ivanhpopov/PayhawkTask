import requests
import json

def check_ip_on_virustotal(ip_address, api_key):
    url = f'https://www.virustotal.com/api/v3/ip_addresses/{ip_address}'
    headers = {"X-Apikey": api_key}
    response = requests.get(url, headers=headers)
    content = json.loads(response.content)
    ip_dict = content
    repuation = ip_dict["data"]["attributes"]["reputation"]
    print(f"Reputation of {ip_address} is: {repuation} (higher is better)")
    
ip_address = input("Give me an IP:")
api_key = '656eb69d98741d422816b890c809f1d8ac78ff4ac5e225a0048ad11cfdb9bd06'

check_ip_on_virustotal(ip_address, api_key)