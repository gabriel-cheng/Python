"""
Dicionários

- Em algumas linguagens de programação, dicionários em Python são conhecidos como Mapas
- É um mapeamento do chave/valor
- São representados por chaves {}
- dicionario = {'chave': 'valor, 'chave': 'valor'}
- Tanto a chave quanto o valor podem ser de qualquer tipo
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
































