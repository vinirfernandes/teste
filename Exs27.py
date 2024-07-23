resp = 's'
media = soma = quant = menor = maior = 0
while resp in "Ss":
    num = int(input("Digite um numero: "))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num 
    resp = str(input("Deseja continuar? [S/N]"))
media = soma / quant
print(f"FIM, vc digitou {quant}, a media entre eles foi {media}, o menor numero foi {menor}, e o maior foi {maior}. ")