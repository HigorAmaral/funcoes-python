def maior(a, b):
    if a > b:
        return a
    else:
        return b

n1 = float(input("Digite o primeiro valor: "))
n2 = float(input("Digite o segundo valor: "))

print("Maior valor:", maior(n1, n2))