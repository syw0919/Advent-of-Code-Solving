import requests
import json
import re

with open('data.json', 'r') as js:
    data = json.load(js)

url = 'https://adventofcode.com/2015/day/5/input'

cookies = data['cookies']

response = requests.get(url, cookies=cookies)

if response.status_code != 200:
    print('wrong cookies')
    exit(0)

words = response.text.split()

vowels = 'aeiou'

nice = 0
naughty = 0

for word in words:
    if sum(word.count(v) for v in vowels) > 2 and re.search(r'([a-z])\1', word) and not ('ab' in word or 'cd' in word or 'pq' in word or 'xy' in word):
        print('Noice', word)
        nice += 1
    else:
        print('Bathds', word)
        naughty += 1

print('Nice words:', nice)
print('Naughty words:', naughty)
