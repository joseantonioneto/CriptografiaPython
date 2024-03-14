from cryptography.fernet import Fernet

chave = input("Insira a chave utilizada para descriptografar: ").encode()
cipher_suite = Fernet(chave)

with open ('arquivo_cifrado.txt','rb') as arquivo_cifrado:
    texto_cifrado = arquivo_cifrado.read()
    texto_decifrado = cipher_suite.decrypt(texto_cifrado)

with open('arquivo_decifrado.txt','wb') as arquivo_decifrado:
    arquivo_decifrado.write(texto_decifrado)
