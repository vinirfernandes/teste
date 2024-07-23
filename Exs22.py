from random import randint

n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
print(" [1] para somar\n [2] para multiplicar\n [3] maior\n [4] novos numeros\n [5] para sair do programa.")

digite = 0
soma = n1 + n2
multiplicacao = n1 * n2

while digite != 5:
    digite = int(input("Escolha uma das opções: "))
    print(" [1] para somar\n [2] para multiplicar\n [3] maior\n [4] novos numeros\n [5] para sair do programa.")
   
    if digite == 1:
        print(f"A soma dos numeros é: {soma}")
    elif digite == 2:
        print(f"A multiplicação dos números é {multiplicacao}")
    elif digite == 3:
        if n1 > n2:
            print(f"Numero maior é {n1}")
        else:
            print(f"Numero maior é {n2}")        
    elif digite == 4:
            n1 = int(input("Digite o primeiro numero: "))
            n2 = int(input("Digite o segundo numero: "))
    elif digite == 5:
        print("Finalizando programa... ")
    else:
        print("Numero inválido. Tente novamente.")