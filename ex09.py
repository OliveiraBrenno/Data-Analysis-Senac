valor = float(input("Digite um valor real: "))
porcentagem = float(input("Digite uma porcentagem sem '%':"))/100

total = valor * porcentagem

print(f"{porcentagem*100}% de {valor} é {total}")
