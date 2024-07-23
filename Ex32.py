num = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    resp = int(input(f"Digite um numero de 0 a 20"))
    if 0 <=  resp <= 20:
        break
    print("Numero invalido tente novamente")

print(f"Voce digitou o numero {num[resp]}")
