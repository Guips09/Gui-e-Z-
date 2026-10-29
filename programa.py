from funcoes import posicao_valida, define_posicoes, preenche_frota

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

for navio in frota:
    tamanho = tamanhos[navio]

    while len(frota[navio]) < quantidades[navio]:
        print(f"Insira as informações referentes ao navio {navio} que possui tamanho {tamanho}")
        linha = int(input("Linha: "))
        coluna = int(input("Coluna: "))

        if navio != "submarino":
            opcao = int(input("[1] Vertical [2] Horizontal >"))

            if opcao == 1:
                orientacao = "vertical"
            elif opcao == 2:
                orientacao = "horizontal"
            else:
                continue
        else:
            orientacao = "vertical"

        if posicao_valida(frota, linha, coluna, orientacao, tamanho):
            frota = preenche_frota(
                frota, navio, linha, coluna, orientacao, tamanho
            )
        else:
            print("Esta posição não está válida!")

print(frota)