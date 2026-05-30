cargo = input("\n Informe seu cargo: ").lower()
salarioBruto = 0

if cargo == "caixa":
    salarioBruto = 1500
elif cargo == "vendedor":
    salarioBruto = 2400
elif cargo == "gerente":
    salarioBruto = 4000
else:
    print("\nCargo não identificado!\n")
    exit()

if salarioBruto > 2000:
    irrf = salarioBruto * 0.14
else:
    irrf = salarioBruto * 0.08

inss = salarioBruto * 0.12
salarioLiquido = salarioBruto - inss - irrf

print("\n---------------------------")
print(f"Salário Bruto: R${salarioBruto}")
print("\n---------Descontos---------\n")
print(f"INSS: R${inss:.2f}")
print(f"IRRF: R${irrf:.2f}")
print("---------------------------")
print(f"Salario Líquido: R${salarioLiquido:.2f}")
print("---------------------------\n")

