import oauth2
import json
import urllib.parse

import pprint


with open('keys.json', 'r') as openFile:
    stringData = openFile.read()
    jsonData = json.loads(stringData)
keys = jsonData


consumer = oauth2.Consumer(
    keys['api']['API_Key'], 
    keys['api']['API_secret_key']
)
token = oauth2.Token(
    keys['token']['Access_token'],
    keys['token']['Access_token_secret']
)

client = oauth2.Client(consumer, token)

query = input('Novo Tweet: ')
query_codificada = urllib.parse.quote(query, safe='')

# method='POST' para fazer requisições post, por padrão é 'GET'
request = client.request(f'https://api.twitter.com/1.1/statuses/update.json?status={query_codificada}', method='POST')

decode_request = request[1].decode() # decodificar a requisição de 'bytes' para 'str'
json_request = json.loads(decode_request) # converte a requisição de 'str' para 'dict'(json)

pprint.pprint(json_request)