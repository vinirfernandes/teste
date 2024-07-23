tabela = ('Corinthians', 'palmeiras', 'Santos', 'Gremio', 'cruzeiro', 'flamengo', 'Vasco', 'Chapecoense', 'Atlético',
           'Botafogo', 'Atletico-Pr', 'Bahia', 'Sao paulo',
           'FluZÃO', 'Sport', 'vitoria', 'Coxa', 'Avai', 'Ponte', 'Atletico go')
print(f"Times {tabela}")
print(f"Os cinco primeiros são{tabela[:5]}")
print(f"Os 4 ultimos são {tabela[16:]}")
print(f'Em ordem alfabetica é {(sorted(tabela))}')
print(f'A chapecoense está {tabela.index("Chapecoense")+1}')
