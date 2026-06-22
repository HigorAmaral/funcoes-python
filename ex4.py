def peso_ideal(altura, sexo):
    if sexo == 1:
        return (62.1 * altura) - 44.7
    elif sexo == 2:
        return (72.7 * altura) - 58

altura = float(input("Digite a altura: "))
sexo = int(input("Digite o sexo (1-Feminino, 2-Masculino): "))

print(f"Peso ideal: {peso_ideal(altura, sexo):.2f} kg")