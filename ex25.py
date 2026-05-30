valores = []

for i in range(5):
    a = int(input("Digite um valor inteiro: "))
    valores.append(a)

for i in range(5):
    a = i
    if valores[a] % 2 == 0:
        print(f"{valores[a]} é par")
    else:
        print(f"{valores[a]} é impar")
