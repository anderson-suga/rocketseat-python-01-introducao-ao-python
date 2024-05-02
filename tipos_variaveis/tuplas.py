"""
    A tupla é uma coleção ordenada e imutável de elementos. 
    Isso significa que, uma vez criada, não podemos modificar seus elementos. 
    Podemos criar uma tupla usando parênteses e acessar seus elementos da mesma forma que uma lista. 
    Além disso, a tupla possui dois métodos úteis: o método count, que retorna a quantidade de vezes 
    que um elemento aparece na tupla, e o método índice, que retorna o índice da primeira ocorrência 
    de um elemento na tupla.
"""


# Criando uma tupla de exemplo
minha_tupla = (1, 2, 2, 3, 4)

print("Minha tupla:", minha_tupla)

print("minha_tupla[0]:", minha_tupla[0])
print("minha_tupla[2]:", minha_tupla[2])
print("minha_tupla[-1]:", minha_tupla[-1])

# Método count
contagem = minha_tupla.count(2)
print("Quantidade de vezes que o elemento 2 aparece:", contagem)

indice = minha_tupla.index(3)
print("Indice da primeira ocorrência do elemento 3:", indice)