# BIBLIOTECAS
import requests
import json


try:

    # CORES
    cor = {'zero':'\033[00;00;00m', 'red':'\033[00;31m', 'reverseRed':'\033[07;31m', 'sub':'\033[04m', 'boldRed':'\033[01;31m'}



    # TÍTULO
    print("{}ctrl+c{} para sair\n".format(cor['sub'], cor['zero']))
    print("{}❮ {}CONSULTAR FILMES{} ❯".format(cor['red'], cor['reverseRed'], cor['red']))
    print("{}\n".format(cor['zero']))



    # COLETA DE DADOS
    filme = input("{}Filme{} ▶ ".format(cor['reverseRed'], cor['red']))
    print(cor['zero'])



    # FAZ A REQUISIÇÃO DA API
    requisicao = requests.get('http://www.omdbapi.com/?apikey=38904b3&t={}'.format(filme))

    # CONVERTE OS DADOS PARA JSON
    dados = json.loads(requisicao.text)



    # TENTA MOSTRAR AS INFORMAÇÕES ADQUIRIDAS OU MOSTRA UM ERRO
    try:
        print("""{}
Título ➤ {}\n
Lançameto ➤ {}\n
Classificação imdb ➤ {}\n
Gênero ➤ {}\n
País ➤ {}\n
Prémios ➤ {}\n
Sinopse ➤ {}\n
{}""".format(cor['boldRed'], dados['Title'], dados['Released'], dados['imdbRating'], dados['Genre'], dados['Country'], dados['Awards'], dados['Plot'], cor['zero']))
    except:
        print("algo deu errado! o nome do filme deve estar digitado incorretamente ou você não possui conexão com a internet.")
        print("\n")

except KeyboardInterrupt: # MENSAGEM A SER EXIBIDA QUANDO OUVER A SAIDA MANUAL DO TECLADO (CTRL+C)

    print("{}\n\nSAINDO...".format(cor['zero']))