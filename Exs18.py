#maior = 0print(f"O menor peso foi de {menor}")#

maior = 0
menor = float('inf')
for i in range(5):
    p = float(input('Peso: '))
    if p>maior:
        maior = p
    if p<menor:
        menor = p
print(f'Dentre esses, o maior peso foi {maior}kg e o menor foi {menor}kg ') 
