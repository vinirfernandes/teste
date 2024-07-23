from random import randint
pc = randint(0, 10)
num = int(input("Digite um número de 0 a 10: "))
erros = 0
while num != pc:
    num = int(input("Errou infelizmente, tente novamente: "))
    erros += 1
    if num > pc:
        print("Um pouco menos")
    else:
        print("Um pouco mais")
print(f"Acertou, depois de {erros} tentativas. Parabéns!")