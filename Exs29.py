while True:
    n = int(input("Quer ver a tabuada de qual numero: "))
    if n < 0:
        break
    for c in range (1, 11):
        tabuada = n * c        
        print(f"A tabuada do numero {n} X {c} = {tabuada}")
print(f"Programa encerrado! ")
    