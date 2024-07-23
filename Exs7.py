peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / (altura * altura)

print(f"Seu imc é {imc:.1f}")

match imc:
    case 18.5:
        print(f"Voce esta abaixo do peso {imc:.1f}")

    case  25:
        print(f"Voce está no peso ideal {imc:.1f}")
    case 30:
        print(f"Voce está com sobrepeso {imc:.2f}")
    case 40:
        print(f"Voce está obeso {imc:.1f}")
    