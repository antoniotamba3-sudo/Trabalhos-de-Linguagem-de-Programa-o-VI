from functools import reduce
numeros = [2, 3, 4, 5,6,7]
soma_total = reduce(lambda x, y: x + y, numeros)
print(f"Soma total: {soma_total}") # Saída: 27
produto_total = reduce(lambda x, y: x * y, numeros)
print(f"Produto total: {produto_total}") # Saída: 5040

