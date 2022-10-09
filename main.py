alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

# função de codificação
def encrypt(msg, num):
    encrypted_msg = ""
    # para cada caracter na mensagem
    for i in msg:
        # se o caracter estiver no alphabet
        if i in alphabet:
            # mudar o caracter shift casas para frente
            new_index = alphabet.index(i) + num
            new_index %= len(alphabet)
            encrypted_msg += alphabet[new_index]
        # se o caracter não estiver no alphabet
        else:
            # adicionar à mensagem encriptada(preservar espaços)
            encrypted_msg += i
        # escrever no terminal a mensagem criptografada
    print(f"Essa é a mensagem codificada: {encrypted_msg}")


# função de decodificação com chave
def decrypt(msg, num):
    decrypted_msg = ""
    # para cada caracter na mensagem
    for i in msg:
        # se o caracter estiver no alphabet
        if i in alphabet:
            # mudar o caracter shift casas para trás
            new_index = alphabet.index(i) - num
            new_index %= len(alphabet)
            decrypted_msg += alphabet[new_index]
        # se o caracter não estiver no alphabet
        elif i not in alphabet:
            # adicionar à mensagem encriptada(preservar espaços)
            decrypted_msg += i
        # escrever no terminal a mensagem decriptografada
    print(f"Essa é a mensagem decodificada: {decrypted_msg}")



# função main
def main():
    correct_direction = False
    # Enquanto a direção for errada
    while not correct_direction:
        # pedir para o usuário escrever a direção
        direction = input("Escolha entre codificar ou decodificar:\n")
        # caso a direção for codificar
        if direction == "codificar":
            correct_direction = True  # <-coloca a direção como certa
            # pede o texto e o número de vezes que o usuário deseja mover cada letra
            text = input("Digite sua mensagem:\n").lower()
            shift = 13
            encrypt(text, shift)

        # caso a direção for decodificar com chave
        elif direction == "decodificar":
            correct_direction = True  # <-coloca a direção como certa
            # pede o texto e o número de vezes que o usuário deseja mover cada letra
            text = input("Digite sua mensagem:\n").lower()
            shift = 13
            decrypt(text, shift)

        else:
            # Imprime no terminal a mensagem de valor inválido
            print("Valor inválido!\n Tente novamente!")


main()
