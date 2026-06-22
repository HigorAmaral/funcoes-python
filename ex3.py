def calcular_media(n1, n2):
    media = (n1 + n2) / 2
    print(f"Média: {media:.1f}")

    if media >= 6:
        print("PARABÉNS! Você foi aprovado!")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

calcular_media(nota1, nota2)