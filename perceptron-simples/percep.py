pesos = [0, 0, 0, 0]

x = [[1, 0, 0, 0], [1, 1, 0, 0], [1, 1, 1, 0], [1, 0, 1, 1], [1, 1, 0, 1], [1, 1,1,1]]

y = [1, 1, 1, 1, -1, -1]  # saida and

epoch = 100 # maximo épocas
eta = 0.2 # taxa de aprendizagem

for _ in range(epoch):
    erros = 0
    for i in range(len(x)):
        soma = 0
        for j in range(len(x[i])):
            soma += x[i][j] * pesos[j]
        saida = 1 if soma > 0 else -1
        erro = y[i] - saida
        if saida != y[i]:
            erros += 1
            for j in range(len(pesos)):
                pesos[j] += eta * x[i][j] * erro
    if erros == 0:
        print(f"iterações treino: {_}")
        break


def teste(x):
    soma = 0
    for i in range(len(x)):
        soma += x[i] * pesos[i]
    return 1 if soma > 0 else -1


print(f"pesos: {pesos}")
print(f"bias: {pesos[0]}")
print("testes:")
for entrada in x:
    print(f"x = {entrada}, saida = {teste(entrada)}")
