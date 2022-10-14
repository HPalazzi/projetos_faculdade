import base64, os

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_PKCS1_v1_5

class RsaHelper():
    def __init__(self, pathToPem=None, nameFile="criypto.pem", createPrivate=False):

        # Se o caminho para o diretorio que o usuario passar não existir nós criaremos um diretorio PRIVADO

        if pathToPem==None:
            pathToPem = os.path.expanduser("~")
        if not os.path.exists(pathToPem):
            os.makedirs(pathToPem)
        if not os.path.exists(pathToPem + "/.ssh"):
            os.makedirs(pathToPem + "/.ssh")
        
        # Nomeando os caminhos dos diretorios que criamos

        self.pathToPrivate = pathToPem + "/.ssh/private_" + nameFile
        self.pathToPublic = pathToPem + "/.ssh/public_" + nameFile
        self.keyPublic = None
        self.keyPrivate = None
        # Se a chave Privada não existir:
        
        if not os.path.exists(self.pathToPrivate and createPrivate == True):
            self.keyPrivate = RSA.generate(1024)

            # Logo, tambem criaremos a chave Publica

            self.keyPublic = self.keyPrivate.publickey()
            if not os.path.exists(self.pathToPrivate):
                with open (self.pathToPrivate, "bw") as privateFile:
                    privateFile.write(self.keyPrivate.exportKey())
            if not os.path.exists(self.pathToPublic):
                with open (self.pathToPublic, "bw") as publicFile:
                    publicFile.write(self.keyPublic.exportKey())
        else:
            if os.path.exists(self.pathToPublic):
                with open(self.pathToPublic, "rb") as k:
                    self.keyPublic = RSA.importKey(k.read())
            if os.path.exists(self.pathToPrivate):
                with open(self.pathToPrivate, "rb") as k:
                    self.keyPrivate = RSA.importKey(k.read());           
    
    def encrypt(self, data):
        
        # Depois daquela patifaria no init, pega essa gostosa de 2 linhas

        cipher = Cipher_PKCS1_v1_5.new(self.keyPublic)
        return base64.b64encode(cipher.encrypt(data.encode("utf-8"))).decode()
    def decrypt(self, data):
        cipher = Cipher_PKCS1_v1_5.new(self.keyPrivate)
        return cipher.decrypt(base64.b64decode(data.encode()), None).decode()

rsa = RsaHelper(pathToPem="/tmp", nameFile="criypto.pem", createPrivate=True) 
mensagem = input("O que você quer passar pro mundo? ")
criptografado = rsa.encrypt(mensagem)
print(criptografado)
print(rsa.decrypt(criptografado))



# Glossario:
# Pem = Lugar na memoria onde guardamos as nossas chaves publicas e privadas