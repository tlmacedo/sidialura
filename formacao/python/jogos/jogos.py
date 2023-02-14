import forca
import adivinhacao


def jogar():
    print("*************************************************")
    print("************** Escolha o seu jogo! **************")
    print("*************************************************")

    print("(1)-Forca (2)-Adivinhação")

    jogo = int(input("Qual jogo? "))
    while jogo < 1 or jogo > 2:
        jogo = int(input("Jogo {} não é válido, defina um jogo válido: ".format(jogo)))

    match jogo:
        case 1:
            print("Jogando forca")
            forca.jogar()
        case 2:
            print("Jogando adivinhação")
            adivinhacao.jogar()


if __name__ == "__main__":
    jogar()
