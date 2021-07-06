"""
Tuplas

Diferenças:
    - São compostas por parênteses
    - Tão são imutáveis, como as contantes, não podem ser alteradas.

- São considerado tuplas:
    - tupla1 = (1, 2)
    - tupla2 = 1, 2
    - tupla3 = 1,
"""
"""
Tipos de tuplas
"""
tupla1 = ('Gabriel', 'Carvalho', 2, 3, 'Souza')
print(tupla1)
print(type(tupla1))

"""
Isto também é considera um tupla
"""
tupla2 = 'Gabriel', 2, 'Carvalho', 4, 'Souza'
print(tupla2)

"""
Tuplas são definidas pela vírgula, não pelo uso do parêntese
"""
tupla3 = (4) # Não é uma tupla, mas é lido formato int
print(tupla3)
print(type(tupla3))

tupla4 = (4,)
print(tupla4)
print(type(tupla4))
###########################################################################
"""
Tuplas com range
"""

tupla = tuple(range(10))
print(tupla)
print(tupla)



