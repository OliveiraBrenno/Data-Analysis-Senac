valor = float(input("Digite um valor inteiro não negativo: "))

if valor.is_integer() == False and valor < 0:
    print(f"{valor} não é inteiro e nem positivo")

elif valor.is_integer() == False:
    print(f"{valor} não é inteiro")

elif valor < 0:
    print(f"{valor} é negativo")

elif 0 <= valor <= 10:
    print(f"{valor} está entre 0 e 10")

elif 11 <= valor <= 20:
    print(f"{valor} está entre 11 e 20")

elif 21 <= valor <= 30:
    print(f"{valor} está entre 21 e 30")

else:
    print(f"{valor} é maior que 30")

       
 