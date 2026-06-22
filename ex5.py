def poligono(lados, medida):
    if lados == 3:
        perimetro = lados * medida
        print("TRIÂNGULO")
        print("Perímetro:", perimetro)

    elif lados == 4:
        area = medida ** 2
        print("QUADRADO")
        print("Área:", area)

    elif lados == 5:
        print("PENTÁGONO")

lados = int(input("Número de lados: "))
medida = float(input("Medida do lado: "))

poligono(lados, medida)