import os, base64, random;
 
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes;
 
class AesHelper():
    # Inicialização - Será criado o construtor da classe AesHelper

    def __init__(self, key=None, iv=None): # Lembrando que IV = Vetor de Incialização
        if (key==None):                    # Key = chave - Mesmo sentido da Cifra de Cézar
            self.key = os.urandom(32)
        else:
            self.key = key
        if iv == None:
            self.iv = os.urandom(16)
        else:
            self.iv = iv
        self.cipher = Cipher(algorithms.AES(self.key), modes.CBC(self.iv))
    
    # Método de Criptografia

    def encrypt(self, message):
        message = base64.b64encode(message.encode()).decode()
        for i in range( 16 - (len(message)  % 16) ):# 16 é a quantidade de Bytes do bloco de criptografia
            message += " "
        encryptor = self.cipher.encryptor()
        return encryptor.update(message.encode("utf-8")) + encryptor.finalize()
    
    # Método de Descriptografia

    def decrypt(self, message):
        decryptor = self.cipher.decryptor()
        return base64.b64decode( (decryptor.update(message) + decryptor.finalize()).decode("utf-8") ).decode("utf-8")  

if __name__ == "__main__":
	ae = AesHelper()
	criptografado = ae.encrypt(input("Digite o texto a ser criptografado: "))
	print(criptografado)
	print(ae.decrypt(criptografado))
