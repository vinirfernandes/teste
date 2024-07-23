num = int(input("Digite um numero = "))
print ("1 para binário, 2 para octal ou 3 para hexadecimal. ")
opcao = int(input("Escolha uma opção: "))
if opcao == 1:
    print (bin(num))

elif opcao == 2:
    print ("O valor Octal é : ", oct(num))

elif opcao == 3:
    print(f"O valor Hexadecimal é: {hex(num)} ")
else:
    print("opcao inválida! ")


