import requests
import json

with open('data.json', 'r') as js:
    data = json.load(js)

url = 'https://adventofcode.com/2015/day/11/input'

cookies = data['cookies']

response = requests.get(url, cookies=cookies)

if response.status_code != 200:
    print('wrong cookies')
    exit(0)

password = response.text.strip()

def increment(password):
    password = list(map(lambda x: ord(x) - ord('a'), password)).reverse()
    
    print(password)
    carry = 0
    for i in reversed(range(len(password))):
        pass

increment(password)