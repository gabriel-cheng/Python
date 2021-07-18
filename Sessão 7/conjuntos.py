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
s = set({1, 2, 3, 4, 5, 5, 6, 7, 3, 2, 1})

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







