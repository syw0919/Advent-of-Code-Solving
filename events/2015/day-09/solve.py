import requests
import json

with open('data.json', 'r') as js:
    data = json.load(js)

url = 'https://adventofcode.com/2015/day/9/input'

cookies = data['cookies']

response = requests.get(url, cookies=cookies)

if response.status_code != 200:
    print('wrong cookies')
    exit(0)

data = response.text.splitlines()

graph: dict[dict] = {}

for route in data:
    left, right = route.split(' to ')
    right, dist = right.split(' = ')
    if left not in graph:
        graph[left] = {}
    if right not in graph:
        graph[right] = {}
    
    graph[left][right] = int(dist)
    graph[right][left] = int(dist)

visited = []

def search(loc = None, next_loc = None):
    if loc is None:
        ret = min(search(x) for x in graph)
    else:
        visited.append(loc)
        if next_loc is None:
            ret = min(search(loc, x) for x in graph[loc])
        else:
            ret = graph[loc][next_loc] + (search(next_loc) if next_loc not in visited else 0)
        visited.remove(loc)
    return ret

print(search())