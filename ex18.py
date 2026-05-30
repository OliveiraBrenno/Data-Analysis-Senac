diaSemana = input("Que dia da semana é hoje? ").lower()
horaAtual = int(input("Informe o horário atual sem minutos: "))
horaFim = int(input("Que horas a sua aula termina? "))

if diaSemana == "sexta-feira" and horaAtual >= (horaFim):
    print("Sextou! Você merece pelo menos 2 chopps!!")

elif diaSemana == "sexta-feira" and horaAtual >= horaFim - 1:
    print("Sextou! Você você merece um chopp!")

else:
    print("Ainda não sextou! Não saia da rotina e vá estudar!")