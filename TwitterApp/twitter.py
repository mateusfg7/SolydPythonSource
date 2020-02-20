import json

with open('keys.json', 'r') as openFile:
    stringData = openFile.read()
    jsonData = json.loads(stringData)

keys = jsonData

