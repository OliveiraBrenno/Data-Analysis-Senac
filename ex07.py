peso = float(input("Informe seu peso em quilogramas: "))
altura = float(input("Informe sua altura em metros: "))
imc = peso / (altura * altura)

print(f"Seu IMC é {imc}")

if imc < 18.5:
    print("Você está abaixo do peso")

elif 18.5 < imc < 24.9:
    print("Você está dentro do peso ideal")

else:
    print("Você está acima do peso")

