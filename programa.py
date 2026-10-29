from funcoes import posicao_valida, define_posicoes,preenche_frota

frota = {
    "porta-aviões": [],
    "navio-tanque": [],
    "contratorpedeiro": [],
    "submarino": []
}

while len(frota["porta-aviões"]) < 1:
    print("Insira as informações do porta-aviões que possui tamanho 4")
    linha = int(input("Linha: "))
    coluna = int(input("Coluna: "))
    opcao = int(input("[1] Vertical [2] Horizontal: "))

    if opcao == 1:
        orientacao = "vertical"
    elif opcao == 2:
        orientacao = "horizontal"
    else:
        continue

    if posicao_valida(frota, linha, coluna, orientacao, 4):
        posicoes = define_posicoes(linha, coluna, orientacao, 4)
        frota=preenche_frota(frota,"porta-aviões",linha,coluna,orientacao,4)
    else:
        print("Posição inválida!")


while len(frota["navio-tanque"]) < 2:
    print("Insira as informações do navio-tanque que possui tamanho 3")
    linha = int(input("Linha: "))
    coluna = int(input("Coluna: "))
    opcao = int(input("[1] Vertical [2] Horizontal: "))

    if opcao == 1:
        orientacao = "vertical"
    elif opcao == 2:
        orientacao = "horizontal"
    else:
        continue

    if posicao_valida(frota, linha, coluna, orientacao, 3):
        posicoes = define_posicoes(linha, coluna, orientacao, 3)
        frota=preenche_frota(frota,"navio-tanque",linha,coluna,orientacao,3)
    else:
        print("Posição inválida!")



while len(frota["contratorpedeiro"]) < 3:
    print("Insira as informações do contratorpedeiro que possui tamanho 2")
    linha = int(input("Linha: "))
    coluna = int(input("Coluna: "))
    opcao = int(input("[1] Vertical [2] Horizontal: "))

    if opcao == 1:
        orientacao = "vertical"
    elif opcao == 2:
        orientacao = "horizontal"
    else:
        continue

    if posicao_valida(frota, linha, coluna, orientacao, 2):
        posicoes = define_posicoes(linha, coluna, orientacao, 2)
        frota=preenche_frota(frota,"contratorpedeiro",linha,coluna,orientacao,2)
    else:
        print("Posição inválida!")


while len(frota["submarino"]) < 4:
    print("Insira as informações do submarino que possui tamanho 1")
    linha = int(input("Linha: "))
    coluna = int(input("Coluna: "))

    if posicao_valida(frota, linha, coluna, orientacao, 1):
        posicoes = define_posicoes(linha, coluna, orientacao, 1)
        frota=preenche_frota(frota,"submarino",linha,coluna,orientacao,1)
    else:
        print("Posição inválida!")

print(frota)