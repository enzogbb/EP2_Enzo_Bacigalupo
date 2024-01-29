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

def preenche_frota(posicionamento, nome_navio, frota):
    posicao = define_posicoes(posicionamento)

    nova_embarcacao = {
        "tipo": nome_navio,
        "posicoes": posicao
    }

    frota.append(nova_embarcacao)
    return frota