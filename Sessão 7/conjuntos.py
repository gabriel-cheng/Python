"""
* Conjuntos em Linguagem de Programação faz referência a Teoria dos Conjuntos da matemática
* São chamados de 'Sets' em Python
* Não possuem valores duplicados
* Não possuem valores ordenados
* Não são acessíveis por índice*

* São referenciados por chaves {}
- Diferença entre sets e dicionários:
    - Dicionários tem chaves e valores
    - Sets tem apenas valor
"""
# Forma 1
s = set({1, 2, 3, 4, 5, 5, 6, 7, 3, 2, 1}) # Menos comum

print(s)
print(type(s))
# Não gera erro e ignora os números repetidos
"""
Mais comum
"""
print()
print("Mais comum")
s = {1, 2, 3, 3, 2, 1}

print(s)
print(type(s))

"""
Para verificar se tem algum número no conjunto, utilziar o if
"""
print()
conj = {1, 2, 3}

if 3 in conj:
    print('Tem o 3')
else:
    print('Não tem o 3')

#################################################################
"""
Não tem como ordenar utilizando o sort()

ex: 
conj = {1, 3, 2, 1, 4, 5}
conj.sort()

print(conj)
"""
#################################################################
"""
Revisão de informações
"""

dados = 3, 4, 4, 5, 99, 99, 12, 15, 15, 14
print()
print(f'Total de {len(dados)} elementos')
print()

# Aceitam valores duplicados
lista = list(dados)
print(f'Lista: {lista} com {len(lista)} elementos')
print(type(lista))

# Aceitam valores duplicados
tupla = tuple(dados)
print(f'Tupla: {tupla} com {len(tupla)} elementos')
print(type(tupla))

# Não aceitam chaves duplicadas
dicio = {}.fromkeys(dados, 'dados')
print(f'Dicionário: {dicio} com {len(dicio)} elementos')
print(type(dicio))

# Não aceitam valores duplicados
conj = set(dados)
print(f'Conjuntos: {conj} com {len(conj)} elementos')
print(type(conj))

