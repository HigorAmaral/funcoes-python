def polegadas_para_cm(pol):
    return pol * 2.54

pol = float(input("Digite o valor em polegadas: "))

print(f"{polegadas_para_cm(pol):.2f} cm")