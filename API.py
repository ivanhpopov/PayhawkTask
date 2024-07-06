import requests

def check_ip_on_virustotal(ip_address, api_key):
    url = f'https://www.virustotal.com/api/v3/ip_addresses/{ip_address}'
    headers = {"X-Apikey": api_key}
    response = requests.get(url, headers=headers)
    return response
    
ip = '133.12.32.43'
API_key = input("Please insert your API Key to proceed")

check_ip_on_virustotal(ip, API_key )