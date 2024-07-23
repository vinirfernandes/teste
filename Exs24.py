n1 = int(input("Digite um termo: "))
n2 = int(input("Digite um sua razão: "))

termo = n1
cont = 1
total = 0
continuar = 10

while continuar !=0:
    total = total + continuar
    while cont <= total:
        print(f" {termo} ", end="")
        termo += n2
        cont += 1    
    print("Pause. ")
    continuar = int(input("Quantos mais termos você quer? "))
print('FIM')
