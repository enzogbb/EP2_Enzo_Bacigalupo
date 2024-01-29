import random

# PARA TESTAS O SEU CÓDIGO NA ACADEMIA PYTHON SERÁ NECESSÁRIO COLAR AS FUNÇÕES DESENVOLVIDAS AQUI!!!

# Função para validar a coordenada
def valida_coordenada(coordenada):
    return 0 <= coordenada <= 9

# Função para verificar se o jogador já acertou uma coordenada anteriormente
def jogador_acertou_anteriormente(coordenada, coordenadas_anteriores):
    return coordenada in coordenadas_anteriores

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

def faz_jogada(tabuleiro_oponente, linha, coluna):
    if tabuleiro_oponente[linha][coluna] == 'X':
        print("Você já atirou nessa posição antes!")
        return False

    if tabuleiro_oponente[linha][coluna] == 1:
        print("Você acertou um navio!")
        tabuleiro_oponente[linha][coluna] = 'X'
        return True
    else:
        print("Você errou!")
        tabuleiro_oponente[linha][coluna] = '-'
        return False

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

def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    '''
    tabuleiro_jogador: tabuleiro do jogador
    tabuleiro_oponente: tabuleiro do oponente
    Função monta uma string com a representação dos tabuleiros do jogador e do oponente.
    O tabuleiro do jogador é representado por um tabuleiro com as posições dos navios.
    O tabuleiro do oponente é representado por um tabuleiro com as posições que o jogador já atirou.
    '''

    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '_______________________________      _______________________________\n'

    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item)
                                  for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join(
            [info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
    texto += '_______________________________      _______________________________\n'
    return texto


def gerando_frota_automaticamente():
    '''
    Função gera uma frota de navios de forma aleatória.
    '''
    quantidades = {
        "submarino": {
            "quantidade": 4,
            "tamanho": 1
        },
        "destroyer": {
            "quantidade": 3,
            "tamanho": 2
        },
        "navio-tanque": {
            "quantidade": 2,
            "tamanho": 3
        },
        "porta-aviões": {
            "quantidade": 1,
            "tamanho": 4
        }
    }

    frota = []

    for nome_navio, info in quantidades.items():
        for _ in range(info["quantidade"]):
            dados_de_posicionamento = {
                "tamanho": info["tamanho"],
            }
            dados_de_posicionamento["orientacao"] = random.choice(
                ["vertical", "horizontal"])
            dados_de_posicionamento["linha"] = random.randint(0, 9)
            dados_de_posicionamento["coluna"] = random.randint(0, 9)

            while not posicao_valida(dados_de_posicionamento, frota):
                dados_de_posicionamento["orientacao"] = random.choice(
                    ["vertical", "horizontal"])
                dados_de_posicionamento["linha"] = random.randint(0, 9)
                dados_de_posicionamento["coluna"] = random.randint(0, 9)

            preenche_frota(dados_de_posicionamento, nome_navio, frota)

    return frota

# Função para verificar se todos os navios foram afundados
def afundados(frota, tabuleiro):
    navios_afundados = 0

    for navio in frota:
        afundado = True

        for local in navio['posicoes']:
            linha, coluna = local

            if tabuleiro[linha][coluna] != 'X':
                afundado = False
                break

        if afundado:
            navios_afundados += 1

    return navios_afundados

coordenadas_jogador_anteriores = set()

# Gerando frota de forma aleatório para jogadores
frota_jogador = gerando_frota_automaticamente()
frota_oponente = gerando_frota_automaticamente()

# Criando tabuleiro com as frotas posicionadas
tabuleiro_jogador = posiciona_frota(frota_jogador)
tabuleiro_oponente = posiciona_frota(frota_oponente)
jogando = True
while jogando:

    linha = int(input('Escolha a linha para atirar (0-9): '))
    coluna = int(input('Escolha a coluna para atirar (0-9): '))

    if (linha, coluna) in coordenadas_jogador_anteriores:
        print(f'A posição linha {linha} e coluna {coluna} já foi informada anteriormente!')
        continue

    coordenadas_jogador_anteriores.add((linha, coluna))

    # Imprimindo tabuleiro
    print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))

    # TODO: Implemente aqui a lógica para perguntar a linha que o jogador deseja atirar
    while True:
        try:
            linha_jogador = int(input("Informe a linha desejada (0 a 9): "))
            if not valida_coordenada(linha_jogador):
                print("Linha inválida! Digite um número entre 0 e 9.")
                continue
            break
        except ValueError:
            print("Entrada inválida! Digite um número inteiro.")

    # TODO: Implemente aqui a lógica para perguntar a coluna que o jogador deseja atirar
    while True:
        try:
            coluna_jogador = int(input("Informe a coluna desejada (0 a 9): "))
            if not valida_coordenada(coluna_jogador):
                print("Coluna inválida! Digite um número entre 0 e 9.")
                continue
            break
        except ValueError:
            print("Entrada inválida! Digite um número inteiro.")

    # TODO: Implemente aqui a lógica para verificar se a linha e coluna não foram escolhidas anteriormente
    if jogador_acertou_anteriormente((linha_jogador, coluna_jogador), coordenadas_jogador_anteriores):
        print(f"A posição linha {linha_jogador} e coluna {coluna_jogador} já foi informada anteriormente!")
        continue

    coordenadas_jogador_anteriores.add((linha_jogador, coluna_jogador))

    # TODO: Implemente aqui a lógica para verificar se o jogador derrubou todos os navios do oponente
    resultado_jogada = faz_jogada(tabuleiro_oponente, linha_jogador, coluna_jogador)

    if afundados(frota_oponente, tabuleiro_oponente) == len(frota_oponente):
        print("Parabéns! Você derrubou todos os navios do seu oponente!")
        jogando = False
        break

# INCOMPLETO - Não consegui avançar