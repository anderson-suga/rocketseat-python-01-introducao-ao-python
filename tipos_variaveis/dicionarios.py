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