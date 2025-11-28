from collections import Counter

nomes = ["Ana", "Ana", "joao", "maria", "ana"]

# tudo minúsculo
nomes = [nome.lower() for nome in nomes]

# contar
contagem = Counter(nomes)

print(contagem)






