valor1 = float(input("Insira o primeiro valor: "))
valor2 = float(input("Insira o segundo valor: "))

if valor1 > valor2:
    print(f"{valor1} é maior que {valor2}")
elif valor2 > valor1:
    print(f"{valor2} é maior que {valor1}")
else:
    print("Os dois valores são iguais!")
