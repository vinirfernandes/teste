valor_casa = float(input("Digite o valor da casa? "))
salario = float(input("Digite o seu salário? "))
anos = int(input("Digite em quantos anos você quer pagar! "))
valor_prestacao = valor_casa / (12*anos)

if valor_prestacao <= 0.3 * salario:
    print ("Você pode fazer o emprestimo!")

else:
    print("Infelizmente você não pode fazer o empréstimo :(")