temp = float(input("Informe a temperatura atual em °C: "))

if temp < 18:
    print(f"A temperatura de {temp} está amena")
elif 18 <= temp <= 30:
    print(f"A temperatura de {temp} está agradável")
else:
    print(f"A temperatura de {temp} está quente")