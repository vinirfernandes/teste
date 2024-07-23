from random import randint

itens = ('Pedra', 'Papel', 'Tesoura')

computador = randint(0,2)
print("Escolha a sua jogada, [0] Pedra, [1] Papel, [2] Tesoura.")

jogador1 = int(input("Qual é a sua jogada? "))
print(f"Você escolheu {itens[jogador1]}.")
print(f"Computador escolheu {itens[computador]}.")

if computador == 0:
    if jogador1 == 0: 
        print("Os dois jogaram pedra, portanto empate!! ")
    
    elif jogador1 == 1:
        print(f"O computador escolheu {itens[computador]} e o jogador escolheu; {itens[jogador1]}, portanto jogador GANHOU!!!! ")

    elif jogador1 == 2:
        print(f"O computador escolheu {itens[computador]} e o jogador escolheu; {itens[jogador1]}, portanto computador GANHOU!!!! ")

if computador == 1:
    if jogador1 == 0:
        print(f"o Jogador escolheu {itens[jogador1]}, e computador escolheu {itens[computador]}, COMPUTADOR VENCEU!!!")
    elif jogador1 == 1:
        print(f"EMPATE AMBOS JOGARAM PAPEL")
    elif jogador1 == 2:
        print(f"O jogador escolheu {itens[jogador1]}, e o computador {itens[computador]}, portanto JOGADOR VENCEU!!! ")

if computador == 2:
    if jogador1 == 0:
        print (f"O Jogador escolheu {itens[jogador1]}, e o computador escolheu {itens[computador]}, portanto JOGADOR VENCEU")

    elif jogador1 == 1:
        print (f"O jogador escolheu {itens[jogador1]}, o computador escolheu {itens[computador]}, portanto  ")
    
    elif jogador1 ==2:
        print("EMPATE O COMPUTADOR TAMBEM ESCOLHEU TESOURA.")

else:
    ("opção invalida")