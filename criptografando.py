from cryptography.fernet import Fernet
import socket


chave = Fernet.generate_key()

cipher_suite = Fernet(chave)


with open ('arquivo.txt', 'rb') as arquivo:
    texto = arquivo.read()
    texto_cifrado = cipher_suite.encrypt(texto)

with open ('arquivo_cifrado.txt', 'wb') as arquivo_cifrado:
    arquivo_cifrado.write(texto_cifrado)

with open ('arquivo_cifrado.txt','rb') as arquivo_cifrado:
    texto_cifrado = arquivo_cifrado.read()
    texto_decifrado = cipher_suite.decrypt(texto_cifrado)

with open('arquivo_decifrado.txt','wb') as arquivo_decifrado:
    arquivo_decifrado.write(texto_decifrado)

server_address = ('127.0.0.1', 5000)

MSG = cipher_suite
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(server_address)
s.sendall(str.encode(MSG))
data = s.recv(1024)
s.close()
