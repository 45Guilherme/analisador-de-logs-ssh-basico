with open("dados.txt", "w") as arquivo:
     arquivo.write("linha 1\n")
     arquivo.write("linha 2\n")
     arquivo.write("linha 3\n")
     arquivo.write("linha 4\n")
     arquivo.write("linha 5\n")
     arquivo.write("linha 6\n")

with open("dados.txt", "r") as arquivo:
  linhas = arquivo.readlines()  

total = len(linhas)
print("o total de linhas é: ", total)

if total == 3:
     print(linhas)

