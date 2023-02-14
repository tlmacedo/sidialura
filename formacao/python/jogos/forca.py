import random


def inicializa_letras_acertadas(palavra):
    return ['_' for letra in palavra]


def jogar():
    imprime_mensagem_abertura()

    palavra_secreta = escolhe_palavra_secreta("frutas.txt")

    palavra_forca = inicializa_letras_acertadas(palavra_secreta)

    print('a palavra secreta tem [{}] letras'.format(len(palavra_forca)))

    erros_max = 7
    erros = 0
    chutes = []
    while erros <= erros_max:
        chute = str(input("Qual o letra vc chuta? "))[:1].strip().lower()
        chutes += chute

        if chute in palavra_secreta: \
            marca_chute_correto(palavra_secreta, chute, palavra_forca)
        else:
            erros += 1
            desenha_forca(erros)

        if "_" not in palavra_forca: break

        print(palavra_forca)

    if erros >= erros_max:
        imprime_mensagem_perdedor(palavra_secreta)
    else:
        imprime_mensagem_vencedor()


def imprime_mensagem_perdedor(palavra_secreta):
    print("*********************************")
    print("*   Puxa, você foi enforcado!   *")
    print("* A palavra era {} *".format(palavra_secreta))
    print("*********************************")
    print("*                               *")
    print("*        _______________        *")
    print("*       /               \       *")
    print("*      /                 \      *")
    print("*   /\/                   \/\   *")
    print("*   \ |   XXXX     XXXX   | /   *")
    print("*    \|   XXXX     XXXX   |/    *")
    print("*     |   XXX       XXX   |     *")
    print("*     |                   |     *")
    print("*     \__      XXX      __/     *")
    print("*       |\     XXX     /|       *")
    print("*       | |           | |       *")
    print("*       | I I I I I I I |       *")
    print("*       |  I I I I I I  |       *")
    print("*       \_             _/       *")
    print("*         \_         _/         *")
    print("*           \_______/           *")
    print("*                               *")
    print("*********************************")


def imprime_mensagem_vencedor():
    print("*********************************")
    print("**** Parabéns, você ganhou!! ****")
    print("*********************************")
    print("*                               *")
    print("*          ___________          *")
    print("*         '._==_==_=_.'         *")
    print("*         .-\\:      /-.        *")
    print("*        | (|:.     |) |        *")
    print("*         '-|:.     |-'         *")
    print("*           \\::.    /          *")
    print("*            '::. .'            *")
    print("*              ) (              *")
    print("*            _.' '._            *")
    print("*           '-------'           *")
    print("*                               *")
    print("*********************************")


def desenha_forca(erros):
    print("*********************************")
    print("*            _______            *")
    print("*           |/      |           *")

    if (erros == 1):
        print("*           |      (_)          *")
        print("*           |                   *")
        print("*           |                   *")
        print("*           |                   *")

    if (erros == 2):
        print("*           |      (_)          *")
        print("*           |      \            *")
        print("*           |                   *")
        print("*           |                   *")

    if (erros == 3):
        print("*           |      (_)          *")
        print("*           |      \|           *")
        print("*           |                   *")
        print("*           |                   *")

    if (erros == 4):
        print("*           |      (_)          *")
        print("*           |      \|/          *")
        print("*           |                   *")
        print("*           |                   *")

    if (erros == 5):
        print("*           |      (_)          *")
        print("*           |      \|/          *")
        print("*           |       |           *")
        print("*           |                   *")

    if (erros == 6):
        print("*           |      (_)          *")
        print("*           |      \|/          *")
        print("*           |       |           *")
        print("*           |      /            *")

    if (erros == 7):
        print("*           |      (_)          *")
        print("*           |      \|/          *")
        print("*           |       |           *")
        print("*           |      / \          *")

    print("*           |                   *")
    print("*          _|___                *")
    print("*                               *")
    print("*********************************")


def imprime_mensagem_abertura():
    print("*********************************")
    print("*  Bem vindo ao jogo de Forca!  *")
    print("*********************************")


def escolhe_palavra_secreta(nome_arquivo='frutas.txt'):
    arquivo_palavras = open(nome_arquivo, 'r')
    palavras_sorteio = []
    for linha in arquivo_palavras:
        palavras_sorteio.append(linha.strip())
    arquivo_palavras.close()
    palavra_secreta = palavras_sorteio[random.randrange(0, len(palavras_sorteio))]
    return palavra_secreta


def marca_chute_correto(palavra_secreta, chute, palavra_forca):
    index = 0
    for letra_secreta in palavra_secreta:
        if chute == letra_secreta:
            palavra_forca[index] = chute
        index += 1


if __name__ == "__main__":
    jogar()
