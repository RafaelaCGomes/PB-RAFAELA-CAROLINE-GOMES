import hashlib

while True:
    mensagem = input("Digite sua mensagem ou E para sair: ")

    if mensagem.lower() == "e":
        print("Saindo")
        break

    hash_mens = hashlib.sha1(mensagem.encode())
    hash_Hexadecimal = hash_mens.hexdigest()
    print(hash_Hexadecimal)
