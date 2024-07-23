n1 = int(input("Escolha um número: "))
n2 = int(input("Escolha outro número: "))
if n1 > n2:
    print(f"O número que você escolheu {n1}, é maior que {n2}.")
elif n2 <n1:
    print(f"O Segundo número {n2} que você escolheu é maior que {n1}!")
elif n1 == n2:
    print(f"Não existe valor maior ou menor, {n1} e {n2}, são iguais!")
