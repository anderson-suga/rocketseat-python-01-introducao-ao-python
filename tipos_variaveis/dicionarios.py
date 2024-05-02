"""
    Um dicionário é uma coleção não ordenada de pares chave-valor. 
    Podemos criar um dicionário usando chaves e armazenar informações dentro dele. 
    Cada chave é importante para acessar a informação posteriormente. 
    Podemos adicionar várias chaves e valores ao dicionário, inclusive outros dicionários. 
    Podemos exibir o dicionário usando a função print e acessar os valores usando as chaves. 
    Se tentarmos acessar uma chave que não existe, receberemos uma exceção KeyError. 
    Podemos adicionar novas chaves ao dicionário mesmo depois de criá-lo.
"""  

# Criando um dicionário de exemplo
pessoa = {"nome": "João", "idade": 30, "cidade": "São Paulo"}

# Exibindo o dicionário
print("Meu dicionário de exemplo:", pessoa)

# Acessando valores por chave
print("Nome:", pessoa["nome"])
print("Idade:", pessoa["idade"])
print("Cidade:", pessoa["cidade"])

pessoa["sobrenome"] = "Silva"
print("Sobrenome", pessoa["sobrenome"])

pessoa["idade"] = 31
print("Idade atualizada:", pessoa["idade"])

# Removendo um par chave-valor
del pessoa["sobrenome"]
print("Meu dicionário de exemplo:", pessoa)

# Métodos: keys(), values(), items()
chaves = list(pessoa.keys())
print("Chaves do dicionário:", chaves)
print("Primeira chave:", chaves[0])

# Métodos values
valores = list(pessoa.values())
print("Valores do dicionário:", valores)
print("Primeiro valor do dicionário:", valores[0])

# Métodos items
itens = list(pessoa.items())
print("Pares chave-valor do dicionário:", itens)
print("Primeira chave-valor: %s = %s" % (itens[0][0], itens[0][1]))