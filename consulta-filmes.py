import requests
import json


print("\n")
print("#### CONSULTAR FILMES ####")
print("\n")

filme = input("Nome do Filme: ")
print("\n")


requisicao = requests.get('http://www.omdbapi.com/?apikey=38904b3&t={}'.format(filme))

dados = json.loads(requisicao.text)



try:
    print("""
    Título: {}\n
    Lançameto: {}\n
    Classificação imdb: {}\n
    Gênero: {}\n
    País: {}\n
    Prémios: {}\n
    Sinopse: {}\n
    """.format(dados['Title'], dados['Released'], dados['imdbRating'], dados['Genre'], dados['Country'], dados['Awards'], dados['Plot']))
except:
    print("algo deu errado! o nome do filme deve estar digitado incorretamente ou você não possui conexão com a internet.")
    print("\n")