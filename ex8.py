def dia_semana(numero):
    dias = ["DOM", "SEG", "TER", "QUA", "QUI", "SEX", "SAB"]

    if 1 <= numero <= 7:
        print(dias[numero - 1])
    else:
        print("Erro: dia inválido!")

n = int(input("Digite um número: "))
dia_semana(n)