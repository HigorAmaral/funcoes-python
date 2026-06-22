def mes(numero):
    meses = [
        "Janeiro", "Fevereiro", "Março", "Abril",
        "Maio", "Junho", "Julho", "Agosto",
        "Setembro", "Outubro", "Novembro", "Dezembro"
    ]

    if 1 <= numero <= 12:
        print(meses[numero - 1])
    else:
        print("Erro: mês inválido!")

n = int(input("Digite um número: "))
mes(n)