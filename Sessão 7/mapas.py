"""
Mapas em Python são chamados de dicionários
"""
meses = dict(jan='100', fev='250', mar='400')
print(meses)

# Iterar sobre dicionários
for chave in meses: # Imprime as chaves
    print(chave)

for chave in meses: # Imprime os valores
    print(meses[chave])

for chave in meses:
    print(f"Em {chave} recebi R${meses[chave]},00")

# Função para imprimir chaves
print(meses.keys()) # Isto irá imprimir

