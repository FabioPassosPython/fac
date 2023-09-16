texto = """
A melhor forma de aprender a programar é praticando o que for aprendendo.
"""
texto1 = texto.lower()
print(texto1)

caracteres = len(texto1)
print(f"Este texto tem {caracteres} carcteres.")

print(texto1) 
for i , c in enumerate(texto1):
    if c == "a" or c == "e" or c == "o":
        print(f"A vogal {c} foi encontrada na posição {i}.")
    else:
        continue

texto3 = "Teste de troca de Branch."
print(texto3)