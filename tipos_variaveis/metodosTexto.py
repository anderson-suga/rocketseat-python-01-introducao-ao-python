nome = "Gabriel"
nome_completo = "Gabriel Casemiro"

print(nome.upper())
print(nome.lower())
print(nome)
print(nome[0])

print("\n\n{}".format(nome_completo))

print(nome_completo.count("a"))
print(nome_completo.find("a"))

print("\n\n")

print(nome.encode())
print(nome.encode().decode())

print("\n\n")

print(nome_completo.replace("b","a"))
print(nome_completo.replace("a","123"))

print("\n\n")

print("-".join(nome))
print(nome_completo.split(" "))
print(nome_completo.split())

print("\n\n")

name = "xGabriel Casemirox"
print(name)
print(name.strip("x"))
print(name.strip("a"))
print(name.rstrip("x"))
print(nome_completo.startswith("Ga"))
print(nome_completo.startswith("BE"))
print("el" in nome_completo)
print("abc" in nome_completo)
print("abc" not in nome_completo)

print("\n\n")

try:
    nome[0] = "A"
except Exception as error:
    print("Erro:\n", error) 