preco = float(input("Digite o preço do produto R$: "))
pagamento = int(input("Escolha a forma de pagamento: [1] á vista dinheiro/cheque. [2] á vista no cartão. [3] até 2X no cartão. [4] 3X ou mais no cartão: "))

if pagamento == 1:
    preco1 = preco - (0.1 * preco)
    print(f"O valor do produto á vista no dinheiro/cheque é {preco1}")

elif pagamento == 2:
    preco2 = preco - (0.05 * preco)
    print(f"O valor do produto á vista no cartão é {preco2}")

elif pagamento == 3:
    preco3 = preco / 2
    print(f"O valor do produto á em duas parcelas no cartão é de: {preco3}")

elif pagamento == 4:
    totalpar = preco + (0.2 * preco)
    precof = int(input("Quantas parcelas?"))
    total = totalpar / precof
    print(f"Sua compra será parcelada em {precof}, e o valor de juros {total:.2f}, e o preco do produto será de {totalpar}.")

else:
    print("Opção invalida")