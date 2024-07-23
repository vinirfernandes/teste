n = cont = soma = 0
n = int(input("Digite um numero [999 para parar]: "))
while n != 999:
    cont += 1
    soma += n
    n = int(input("Digite um numero [999 para parar]: "))

print(f"voce digitou {cont} numero e a soma entre eles é: {soma}")