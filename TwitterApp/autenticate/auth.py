def Ler(arquivo):
    with open(arquivo, 'r') as openFile:
        return openFile.read()


print(Ler('test.txt'))