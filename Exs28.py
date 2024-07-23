quant = soma = 0
while True:
    n = int(input("Digite um numero: "))
    if n == 999:
        break
    quant += 1
    soma += n
print(f"vc digitou {quant}, e a soma deles foi {soma}. ")