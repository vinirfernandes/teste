n1 = float(input("Digite sua nota: "))
n2 = float(input("Digite sua outra nota: "))
nf = (n1 + n2) / 2

if nf >= 7.0:
    print(f"Parbéns pela aprovação, sua nota foi {nf}! ")
elif nf >= 5.0 and nf < 7:
    print(f"Você está de recuperação, sua nota foi {nf}! ")
elif nf < 5.0:
    print(f"Você está reprovado, sua nota foi {nf}. ")
