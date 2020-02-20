import oauth2 # biblioteca de autenticação
import json # biblioteca para tratamendo de dados json
import pprint # biblioteca para exibir dados json de forma mais visual

# abre o arquivo contendo as keys
with open('keys.json', 'r') as openFile:
    stringData = openFile.read()
    jsonData = json.loads(stringData)
keys = jsonData

# pega a api key
consumer = oauth2.Consumer(
    keys['api']['API_Key'], 
    keys['api']['API_secret_key']
)
# pega o token key
token = oauth2.Token(
    keys['token']['Access_token'],
    keys['token']['Access_token_secret']
)
# junta a api key e o token key em um cliente
client = oauth2.Client(consumer, token)

query = input('search: ')

# fazer a requisição de uma feature da api (no caso é para fazer pesquisas no twitter)
request = client.request(f'https://api.twitter.com/1.1/search/tweets.json?q={query}')
decode_request = request[1].decode() # decodificar a requisição de 'bytes' para 'str'
json_request = json.loads(decode_request) # converte a requisição de 'str' para 'dict'(json)

tweets = json_request['statuses'][0]

for tweet in json_request['statuses']:
    # pprint.pprint(tweet['user']['name']) # função para printar dados json mais organisadas
    print(f"{tweet['user']['name']}")
    print(f"{tweet['user']['screen_name']}\n")
    print(f"{tweet['text']}")
    print('\n\n\n')