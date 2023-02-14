import random


def inicializa_letras_acertadas(palavra):
    return ['_' for i in palavra]


def jogar():
    imprime_mensagem_abertura()

    palavra_secreta = escolhe_palavra_secreta()

    palavra_forca = inicializa_letras_acertadas(palavra_secreta)
    chutes = []
    enforcou = False
    acertou = False
    repetiu_letra = False

    print('a palavra secreta é ? {} com {} letras'.format(''.join(palavra_forca), len(palavra_forca)))

    while not enforcou and not acertou:
        if len(chutes) > 0 and not repetiu_letra:
            chutes.sort()
            print('\nSeus chutes foram: [{}]'.format(chutes))
            print("forca: {}".format(''.join(palavra_forca)))

        chute = str(input("Qual letra? "))[:1].strip().lower()
        repetiu_letra = chute in chutes
        if repetiu_letra:
            continue
        chutes += chute

        index = 0
        for letra_secreta in palavra_secreta:
            if chute == letra_secreta:
                palavra_forca[index] = chute
            index += 1

            if palavra_secreta == ''.join(palavra_forca):
                acertou = True
                print("\n\n")
                break

        enforcou = len(chutes) == (len(palavra_secreta) * 2)
        # print("forca: {}".format(''.join(palavra_forca)))

    print(
        "\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*" +
        "\n*-*-*-*-*- Acertou -*-*-*-*-*" +
        "\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*" +
        "\nPalavra secreta: {}".format(palavra_secreta) +
        "\nLetras jogadas:  {}".format(chutes) +
        "\nPalavra formada: {}".format(''.join(palavra_forca)) +
        "\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*" +
        "\n*-*-*-*- Fim do jogo -*-*-*-*" +
        "\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")


if __name__ == "__main__":
    jogar()


def imprime_mensagem_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo de Forca!***")
    print("*********************************")


def escolhe_palavra_secreta():
    arquivo = open('palavras.txt', 'r')
    palavras = []
    for linha in arquivo:
        palavras.append(linha.strip())
    arquivo.close()
    palavra_secreta = palavras[random.randrange(0, len(palavras))]
    return palavra_secreta
