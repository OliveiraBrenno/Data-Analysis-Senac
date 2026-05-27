idade = int(input("Informe sua idade: "))
genero = input("Informe seu gênero (M/F): ").upper()

if idade < 18:
    print("Inapto para o alistamento!")

if idade >= 18:
    if genero == "M":
        print("Alistamento concluído!")
    else:
        print("Inapto para o alistamento!")


