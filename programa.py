from funcoes import (posicao_valida, preenche_frota, posiciona_frota,monta_tabuleiros, faz_jogada, afundados)
import random

quantidades = {
    "porta-aviões": 1,
    "navio-tanque": 2,
    "contratorpedeiro": 3,
    "submarino": 4
}

tamanhos = {
    "porta-aviões": 4,
    "navio-tanque": 3,
    "contratorpedeiro": 2,
    "submarino": 1
}

frota = {
    "porta-aviões": [],
    "navio-tanque": [],
    "contratorpedeiro": [],
    "submarino": []
}

frota_oponente = {
    "porta-aviões": [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    "navio-tanque": [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    "contratorpedeiro": [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    "submarino": [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}

for navio in frota:
    tamanho = tamanhos[navio]

    while len(frota[navio]) < quantidades[navio]:
        print(f"Insira as informações referentes ao navio {navio} "f"que possui tamanho {tamanho}")

        linha = int(input("Linha: "))
        coluna = int(input("Coluna: "))

        if navio != "submarino":
            opcao = int(input("[1] Vertical [2] Horizontal >"))

            if opcao == 1:
                orientacao = "vertical"
            elif opcao == 2:
                orientacao = "horizontal"
            else:
                print("Opção inválida!")
                continue
        else:
            orientacao = "vertical"

        if posicao_valida(frota, linha, coluna, orientacao, tamanho):
            frota = preenche_frota(
                frota, navio, linha, coluna, orientacao, tamanho
            )
        else:
            print("Esta posição não está válida!")

jogador = posiciona_frota(frota)
oponente = posiciona_frota(frota_oponente)

jogando = True

while jogando:
    print(monta_tabuleiros(jogador, oponente))

    jogada_valida = False

    while not jogada_valida:
        linha = int(input("Jogador, qual linha deseja atacar? "))

        while linha < 0 or linha > 9:
            print("Linha inválida!")
            linha = int(input("Jogador, qual linha deseja atacar? "))

        coluna = int(input("Jogador, qual coluna deseja atacar? "))

        while coluna < 0 or coluna > 9:
            print("Coluna inválida!")
            coluna = int(input("Jogador, qual coluna deseja atacar? "))

        if oponente[linha][coluna] in ["X", "-"]:
            print(f"A posição linha {linha} e coluna {coluna} ""já foi informada anteriormente!")
        else:
            jogada_valida = True

    oponente = faz_jogada(oponente, linha, coluna)

    if afundados(frota_oponente, oponente) == 10:
        print("Parabéns! Você derrubou todos os navios do seu oponente!")
        jogando = False

    else:
        
        linhao = random.randint(0, 9)
        colunao = random.randint(0, 9)

        while jogador[linhao][colunao] in ["X", "-"]:
            linhao = random.randint(0, 9)
            colunao = random.randint(0, 9)

        print( f"Seu oponente está atacando na linha {linhao} "f"e coluna {colunao}")

        jogador = faz_jogada(jogador, linhao, colunao)

        if afundados(frota, jogador) == 10:
            print("Xi! O oponente derrubou toda a sua frota =(")
            jogando = False