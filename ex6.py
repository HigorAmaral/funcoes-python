def soma_intervalo(n1, n2):
    soma = 0
    for i in range(n1, n2 + 1):
        soma += i
    return soma

n1 = int(input("Digite n1: "))
n2 = int(input("Digite n2: "))

print("Soma =", soma_intervalo(n1, n2))