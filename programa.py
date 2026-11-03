from funcoes import *

frota = {
    "porta-aviões": [],
    "navio-tanque": [],
    "contratorpedeiro": [],
    "submarino": []
}

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

frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}


frota = {
    "porta-aviões": [],
    "navio-tanque": [],
    "contratorpedeiro": [],
    "submarino": []
}

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

frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}


jogador = posiciona_frota(frota)
oponente = posiciona_frota(frota_oponente)

jogando = True

while jogando:
    print(monta_tabuleiros(jogador, oponente))

    posicao_nova = False

    while not posicao_nova:
        jogadal = int(input("Jogador, qual linha deseja atacar? "))

        while jogadal < 0 or jogadal > 9:
            print("Linha inválida!")
            jogadal = int(input("Jogador, qual linha deseja atacar? "))

        jogadac = int(input("Jogador, qual coluna deseja atacar? "))

        while jogadac < 0 or jogadac > 9:
            print("Coluna inválida!")
            jogadac = int(input("Jogador, qual coluna deseja atacar? "))

        if oponente[jogadal][jogadac] in ["X", "-"]:
            print(
                f"A posição linha {jogadal} e coluna {jogadac} "
                "já foi informada anteriormente!"
            )
        else:
            posicao_nova = True

    oponente = faz_jogada(oponente, jogadal, jogadac)

    if afundados(frota_oponente, oponente) == 10:
        print("Parabéns! Você derrubou todos os navios do seu oponente!")
        jogando = False