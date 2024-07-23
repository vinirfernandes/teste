palavras = ('teclado', 'padrao', 'contagem', 'letra', 'ontem', 'sorriu')
for p in palavras:
    for letra in p:
        print(f"\n na palavra temos {p}")
        if letra in 'aeiou':
            print(f" {letra} vogais", end = '')