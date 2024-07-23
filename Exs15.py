num = int(input("Digite um número: "))
tot = 0
for c in range (1, num + 1):   
        if num % c == 0:
            print(f" {c} ", end= '')
            tot += 1
        else:
            print(f"Não é primo")
print(f"O numero {num} foi divisivel {tot} vezes.")