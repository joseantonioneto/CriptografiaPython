from cryptography.fernet import Fernet

chave = Fernet.generate_key()

cipher_suite = Fernet(chave)

with open ('arquivo.txt', 'rb') as arquivo:
    texto = arquivo.read()
    texto_cifrado = cipher_suite.encrypt(texto)

with open ('arquivo_cifrado.txt', 'wb') as arquivo_cifrado:
    arquivo_cifrado.write(texto_cifrado)

print("Chave utilizada para criptografar:", chave)
