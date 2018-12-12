import json

path = 'JSON_1.json'

with open(path, 'r') as f:
    data = json.loads(f.read())
    print(data['player 1']['class'])
