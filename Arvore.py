# Função auxiliar para visualizar
def imprimir_arvore(raiz, nivel=0, prefixo="Raiz: "):
    if raiz is not None:
        print(" " * (nivel * 4) + prefixo + str(raiz.valor))
        if raiz.esquerda or raiz.direita:
            if raiz.esquerda:
                imprimir_arvore(raiz.esquerda, nivel + 1, "E--- ")
            else:
                print(" " * ((nivel + 1) * 4) + "E--- None")
            if raiz.direita:
                imprimir_arvore(raiz.direita, nivel + 1, "D--- ")
            else:
                print(" " * ((nivel + 1) * 4) + "D--- None")