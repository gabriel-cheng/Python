"""
Dicionários

- Em algumas linguagens de programação, dicionários em Python são conhecidos como Mapas
- É um mapeamento do chave/valor
- São representados por chaves {}
- dicionario = {'chave': 'valor, 'chave': 'valor'}
- Tanto a chave quanto o valor podem ser de qualquer tipo
- Podemos utilizar qualquer tipo de dado (int, str, float, bool, dict, tuplas, listas, etc.)
"""
"""
Forma 1 - mais comum
"""
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguay'}
print(paises)
print(type(paises))

"""
Forma 2 - menos comum
"""
paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguay')
print(paises)
print(type(paises))

##########################################################################
"""
Acessando elementos
Forma 1
"""

paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguay')
print(paises['py'])
# print(paises['ru']) # Vai gerar um erro


"""
Forma 2 - Recomendado (Utilizando get)
"""
print(paises.get('br'))
print(paises.get('ru'))

pais = paises.get('py')
pais = paises.get('py', 'Sei lá')

if pais:
    print(f'Encontrei o {pais}')
else:
    print(f'Não encontrei o {pais}')
##########################################################################
"""
Verificando se o elemento está dentro da lista
"""
nomes = dict(
    ga='Gabriel',
    he='Henrique',
    so='Souza'
)

print('ga' in nomes) # É possível verificar somente a chave com este método

if 'ca' in nomes:
    Carvalho = nomes['ca']
##########################################################################
"""
Adicionando elementos em dicionários
- Não podemos ter chaves repetidas
- Caso você adicionar uma chave repetida, será alterado o valor daquela chave, e não adicionado
"""
# Forma 1 - Mais comum
nomes = dict(
    ga='Gabriel',
    he='Henrique',
    so='Souza'
)

print(nomes)

nomes['ca'] = 'Carvalho'

print(nomes)

# Forma 2
novo_nome = {'si': 'Silva'}
print(nomes)

nomes.update(novo_nome) # nomes.update({'si': 'Silva']})   <- Também pode ser utilizado
print(nomes)

# Atualizando conteúdo

nomes['ga'] = 'Rafael'
print(nomes)

nomes.update({'he': 'Antônio'})
print(nomes)

##########################################################################
"""
Deletando elementos

"""
# Forma 1
# Neste caso, o valor é retornado.
nomes = dict(ga='Gabriel', he='Henrique', so='Souza', ca='Carvalho')
print(nomes)

nomes.pop('so')
print(nomes)

# Forma 2 - Forma mais comum
# Neste caso, o valor não é retornado.
del nomes['ca']
print(nomes)








