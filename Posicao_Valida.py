# Define Posições - Ex1
def define_posicoes(posicionamento):
    linha = posicionamento["linha"]
    coluna = posicionamento["coluna"]
    orientacao = posicionamento["orientacao"]
    tamanho = posicionamento["tamanho"]

    posicao = []

    if orientacao == "vertical":
        for i in range(linha, linha + tamanho):
            posicao.append([i, coluna])
    elif orientacao == "horizontal":
        for j in range(coluna, coluna + tamanho):
            posicao.append([linha, j])

    return posicao

# Preenche Frota - Ex2
def preenche_frota(posicionamento, nome_navio, frota):
    posicao = define_posicoes(posicionamento)

    nova_embarcacao = {
        "tipo": nome_navio,
        "posicoes": posicao
    }

    frota.append(nova_embarcacao)
    
    return frota

# Faz Jogada - Ex3
def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    else:
        tabuleiro[linha][coluna] = '-'
    return tabuleiro

# Posiciona Frota - Ex4
def posiciona_frota(frota):
    grid = [[0] * 10 for _ in range(10)]

    for navio in frota:
        tipo_navio = navio["tipo"]
        posicao = navio["posicoes"]

        for pos_grid in posicao:
            linha, coluna = pos_grid
            grid[linha][coluna] = 1

    return grid

# Quantas Embarcações Afundadas - Ex5
def afundados(frota, tabuleiro):
    navios_afundados = 0

    for navio in frota:
        posicao_navio = navio["posicoes"]
        afundado = all(tabuleiro[linha][coluna] == 'X' for linha, coluna in posicao_navio)

        if afundado:
            navios_afundados += 1

    return navios_afundados

# Posicao_Valida - Ex6
def posicao_valida(dados_posicionamento, frota):
    linha = dados_posicionamento["linha"]
    coluna = dados_posicionamento["coluna"]
    orientacao = dados_posicionamento["orientacao"]
    tamanho = dados_posicionamento["tamanho"]

    def define_posicoes(linha, coluna, orientacao, tamanho):
        posicao = []

        if orientacao == "horizontal":
            posicao = [[linha, coluna + i] for i in range(tamanho)]
        elif orientacao == "vertical":
            posicao = [[linha + i, coluna] for i in range(tamanho)]

        return posicao

    nova_posicao = define_posicoes(linha, coluna, orientacao, tamanho)

    for navio in frota:
        posicoes_navio = navio["posicoes"]
        for local in nova_posicao:
            if local in posicoes_navio:
                return False

    return all(0 <= local[0] < 10 and 0 <= local[1] < 10 for local in nova_posicao)