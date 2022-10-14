import base64;
 
from Crypto.Cipher import Salsa20;
from Crypto.Random import get_random_bytes;
 
class SalsaHelper():
    # Construtor do Código
    def __init__(self, key=None):
        if key == None:
            self.key = get_random_bytes(32)
        else:
            self.key = key

    # Método de Criptografia
    def encrypt(self, message):
        cipher = Salsa20.new(key=self.key)
        msg = cipher.nonce + cipher.encrypt(message.encode("utf-8")) # 1
        return base64.b64encode( msg ).decode("utf-8") # 2
    
    # Método de Descriptografia
    def decypt(self, message):
        message = base64.b64decode(message.encode("utf-8"))
        message_nonce = message[:8] # 3
        message_crypt = message[8:]
        cipher = Salsa20.new(key=self.key, nonce=message_nonce)
        return cipher.decrypt(message_crypt).decode("utf-8") # 4

if __name__ == "__main__":
    s = SalsaHelper()
    text = input("Digite o texto a ser criptografado: ")
    encrypted = s.encrypt(text)
    decriptografado = s.decypt(encrypted)
    print("O texto criptografado ficou:",encrypted)
    print("O texto descriptografado ficou:",decriptografado)

# Glossario

# 1. Nonce é um algoritimo que serve para aumentar o nivel de criptografia, garantindo a integridade do código em ambientes externos
# 2. Base 64 é codificar a mensagem passada para uma base de 64 bits
# 3. [:8] e [8:] É separar o nonce criado anteriormente e a mensagem que queremos realmente descriptografar
# 4. Decode é você querer que o obj que foi descriptografado seja passado como string