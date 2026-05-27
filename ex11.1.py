current_date = int(input("Informe a data de hoje no formato ddmmaaaa: "))
birth_date = int(input("Informe a data do seu nascimento no formato ddmmaaaa: "))

birth_day = birth_date // 1000000
birth_month = (birth_date // 10000) % 100
birth_year = birth_date % 10000     

current_day = current_date // 1000000
current_month = (current_date // 10000) % 100
current_year = current_date % 10000 

if birth_year <= current_year - 18 and birth_month <= current_month and birth_day <= current_day:
    print("Maior de idade!")
else:
    print("Menor de idade!")

