def divisivel(x, y):
    if x % y == 0:
        return 1
    else:
        return 0

x = int(input("Digite x: "))
y = int(input("Digite y: "))

print(divisivel(x, y))