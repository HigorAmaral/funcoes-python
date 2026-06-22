import math

def calcular_hipotenusa(cateto_a, cateto_b):
    return math.sqrt(cateto_a**2 + cateto_b**2)

# Programa principal
cateto_a = float(input("Digite o valor do cateto A: "))
cateto_b = float(input("Digite o valor do cateto B: "))

hipotenusa = calcular_hipotenusa(cateto_a, cateto_b)

print(f"Hipotenusa = {hipotenusa:.2f}")