import random


def jogar():
    print("*************************************************")
    print("******* Bem vindo ao jogo de Adivinhação! *******")
    print("*************************************************")

    pontos_inicial: int = 1000
    numero_min: int = 1
    numero_max: int = 100
    numero_secreto: int = random.randrange(numero_min, numero_max + 1)
    niveis_de_dificuldade = [('Facil', 20), ('Medio', 10), ('Dificil', 5)]
    nivel_min: int = 1
    nivel_max: int = len(niveis_de_dificuldade) + 1
    nivel_dificuldade: int = 0
    nivel_dificuldade_index: int
    chute: int
    rodada: int = 1
    strNivel: str
    strChute: str

    niveis_de_dificuldade_exibicao: str = ''
    for i in niveis_de_dificuldade:
        niveis_de_dificuldade_exibicao += '({})-{}  '.format(niveis_de_dificuldade.index(i) + 1, i[0])

    while nivel_dificuldade not in range(nivel_min, nivel_max):
        if nivel_dificuldade is None:
            strNivel = 'Níveis de dificuldade: {}\nQual nível vc quer jogar ? dígite o número referente ao nível ' \
                       'escolhido: ' \
                .format(niveis_de_dificuldade_exibicao)
        else:
            strNivel = "Nível {} não é válido, defina um nível válido: ".format(nivel_dificuldade)

        nivel_dificuldade = int(input(strNivel).strip()[:1])
    nivel_dificuldade_index = nivel_dificuldade - 1

    total_tentativas = niveis_de_dificuldade[nivel_dificuldade_index][1]
    print(
        "\nParabéns o nível de dificuldade escolhido foi o '{}' e vc vai ter [{}] tentativas.\nSua pontuação inicial "
        "é {} pontos".format(niveis_de_dificuldade[nivel_dificuldade_index][0], total_tentativas, pontos_inicial))

    for jogadas in range(rodada, total_tentativas + 1):
        chute = int(input('Tentativa [{}] de [{}].\nDigite um número entre {} e {}: '
                          .format(jogadas, total_tentativas, numero_min, numero_max)).strip())
        while chute not in range(numero_min, numero_max + 1):
            chute = int(
                input('Número [{}] não é válido para o jogo tente um número entre [{}] e [{}]... tente novamente: '
                      .format(chute, numero_min, numero_max)).strip())

        acertou = (chute == numero_secreto)

        if acertou:
            print("Você acertou e fez {} pontos!".format(pontos_inicial))
            break
        else:
            maior = (chute > numero_secreto)
            menor = (chute < numero_secreto)
            pontos_perdidos = abs(numero_secreto - chute)
            pontos_inicial -= pontos_perdidos
            print("Você errou! O seu chute foi {} do que o número secreto.".format("maior" if maior else "menor"))
        print('Sua atual pontuação é de {} pontos.'.format(pontos_inicial))
    print("\nFim do jogo")


if __name__ == "__main__":
    jogar()
