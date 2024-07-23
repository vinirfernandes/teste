produtos = ('lapis', 2.50,
            'caderno', 10.00,
            'Borracha', 1.50,
            'pincel', 3.00,
            'Caneta', 2.00,
            'Apagador', 6.00)
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f"{produtos[pos]:.<30}", end =' ' )
    else:
        print(f"R${produtos[pos]:>7.2f}")