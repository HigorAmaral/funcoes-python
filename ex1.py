def celsius(f):
    return (f - 32) * 5 / 9


f = float(input("Temperatura em Fahrenheit: "))
print(f"Celsius: {celsius(f):.2f}")