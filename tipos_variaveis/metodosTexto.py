nome = "Gabriel"

print(nome.upper())
print(nome.lower())
print(nome)
print(nome[0])

try:
    nome[0] = "A"
except Exception as error:
    print("Erro:\n", error) 