pesos = [0, 0]

x = [[0, 0], [0, 1], [1, 0], [1, 1]]

y = [-1, -1, -1, 1]  # saida and

epoch = 100
eta = 0.5
bias = 0

for _ in range(epoch):
    erros = 0
    for i in range(len(x)):
        soma = 0
        for j in range(len(x[i])):
            soma += x[i][j] * pesos[j]
        soma += bias
        saida = 1 if soma >= 0 else -1
        erro = y[i] - saida
        if saida != y[i]:
            erros += 1
            for j in range(len(pesos)):
                pesos[j] += eta * x[i][j]
            bias += erro
    if erros == 0:
        print(f"iterações treino: {_}")
        break


def teste(x):
    soma = 0
    for i in range(len(x)):
        soma += x[i] * pesos[i]
    soma += bias
    return 1 if soma >= 0 else -1


print(f"pesos: {pesos}")
print(f"bias: {bias}")
print("testes:")
for entrada in x:
    print(f"x = {entrada}, saida = {teste(entrada)}")
