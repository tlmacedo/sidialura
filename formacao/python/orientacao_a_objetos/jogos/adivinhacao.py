import random


def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1, 101)
    print("número: {}".format(int(numero_secreto)))
    total_de_tentativas: int = 0

    pontos = 1000

    print("Qual nível de dificuldade ?")
    print("(1)-Fácil (2)-Médio (3)-Difícil")

    nivel = int(input("Defina o nível: "))
    while nivel < 1 or nivel > 3:
        nivel = int(input("Nível {} não é válido, defina um nível válido: ".format(nivel)))

    match nivel:
        case 1:
            total_de_tentativas = 20
        case 2:
            total_de_tentativas = 10
        case 3:
            total_de_tentativas = 5
        case _:
            print("nível não existe!\ninicie novamente")
            exit(0)

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa, {} de {}.".format(rodada, total_de_tentativas))
        chute = int(input("Digite o número entre 1 e 100: "))
        print("Você digitou", chute)

        if chute < 1 or chute > 100:
            print("Você deve digitar um número entre 1 e 100!")
        else:
            acertou = (chute == numero_secreto)

            if acertou:
                print("Você acertou e fez {} pontos!".format(pontos))
                break
            else:
                maior = (chute > numero_secreto)
                menor = (chute < numero_secreto)
                print("Você errou! O seu chute foi {} do que o número secreto.".format("maior" if maior else "menor"))
                pontos_perdidos = abs(numero_secreto - chute)
                pontos -= pontos_perdidos

    print("Fim do jogo")


if __name__ == "__main__":
    jogar()
