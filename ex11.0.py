current_year = int(input("Informe o ano atual: "))
birth_year = int(input(("Informe o ano do seu nascimento: ")))

if current_year - birth_year >= 18:
    print("Maior de Idade!")
else:
    print("Menor de Idade!")