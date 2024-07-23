from random import randint 
v = 0
while True:
    n = int(input("Digite um numero: "))
    pc = randint(0, 10)
    total = n + pc
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = str(input("Escolha um tipo, par ou impar. [P/I]"))       
        print(f"Voce jogou {n} e o computador {pc}, o total é {total}. ")
        if tipo == 'Pp':
            if total % 2 == 0:           
                print(f"voce venceu {v}")
                v += 1
            else:
                print(f"Voce perdeu")
                break
        elif tipo == "Ii":
            if total % 2 == 1:
                print(f"Voce venceu {v}")
                v += 1
            else:
                print(f"Voce perdeu")
                break
            print("Vamos jogar novamente. ")
    print(f"Game over voce venceu {v} vezes")