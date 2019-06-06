##################################
## script by <Mateus Felipe>    ##
## https://github.com/mateusfg7 ##
## mateusfelipefg77@gmail.com   ##
##################################


# BIBLIOTECAS
import requests
import json

# FUNÇÃO PARA VERIFICAR A CONEXÇAO COM A INTERNET
def internet():
	try:
		requests.get("https://google.com")
		return True
	except:
		return False

# CONDIÇÃO DE EXECUÇÃO COM INTERNET
if internet() == True:

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
        except KeyError:
            print("FILME NÃO ENCONTRADO! o nome pode ter sido digitado incorretamente ou ele é inexistente.")
            print("\n")

    except KeyboardInterrupt: # MENSAGEM A SER EXIBIDA QUANDO OUVER A SAIDA MANUAL DO TECLADO (CTRL+C)

        print("{}\n\nSAINDO...".format(cor['zero']))

else:
    print("\nVocê precisa estar conectado a internet...\n")