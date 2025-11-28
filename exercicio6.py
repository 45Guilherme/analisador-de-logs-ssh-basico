import re
from collections import Counter

# Criar arquivo
with open("ip.txt", "w") as arquivo:
    arquivo.write("Failed password for root from 10.0.0.1 port 2222 ssh2\n")
    arquivo.write("Failed password for root from 10.0.0.2 port 3333 ssh2\n")
    arquivo.write("Failed password for root from 10.0.0.1 port 2222 ssh2\n")
    arquivo.write("Accepted password for admin from 10.0.0.3 port 4444 ssh2\n")
    arquivo.write("Failed password for root from 10.0.0.1 port 2222 ssh2\n")

# Ler arquivo
with open("ip.txt", "r") as arquivo:
    linhas = arquivo.readlines()

# Filtrar falhas
falhas = [linha for linha in linhas if "Failed password" in linha]

print("Total de falhas:", len(falhas))
print()

# Regex para extrair IP
regex = r"from ([\d\.]+) port"

# Coletar IPs
ips = []

for linha in falhas:
    achou = re.search(regex, linha)
    if achou:
        ips.append(achou.group(1))

# Contar IPs
contagem = Counter(ips)

# Imprimir resultado no formato desejado
print("IPs atacantes:")
for ip, quantidade in contagem.items():
    print(f"{ip} \u2192 {quantidade}")
