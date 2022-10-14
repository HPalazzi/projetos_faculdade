# alfabeto = ['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

chave = 3 
mensagem = input("Digite a mensagem que você deseja criptografar: ")
mensagem = mensagem.lower()
tamanhoDaLista = 128 # Quantidade de caracteres ASCII
cifrada = ""

# for letra in mensagem:
#     indice = alfabeto.index(letra)
#     novaLetra = alfabeto[(indice + chave)%tamanhoDaLista]
#     cifrada = cifrada + novaLetra
# print("A entrada foi: {0}".format(mensagem))
# print("A saida foi: {0}".format(cifrada))

for letra in mensagem:
    indice = ord(letra)
    novaLetra = chr((indice + chave)%tamanhoDaLista)
    cifrada = cifrada + novaLetra
print("A entrada foi: {0}".format(mensagem.capitalize()))
print("A saida foi: {0}".format(cifrada.capitalize()))