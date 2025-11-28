# 🔐 Analisador de Logs SSH — Versão Básica

Este projeto é um **analisador simples de logs de tentativas de login SSH**, criado para estudar:

- Leitura de arquivos (`open`, `readlines`)
- Filtragem de texto
- Expressões regulares (Regex)
- Contagem de valores (`collections.Counter`)
- Lógica básica de análise de dados

É o **primeiro passo** para construir um analisador mais avançado no futuro.

---

## 📌 Como funciona

1. O programa cria um arquivo `ip.txt` com vários registros de log simulados.
2. Ele lê o arquivo linha por linha.
3. Filtra apenas as mensagens contendo `"Failed password"`.
4. Usa **Regex** para extrair o IP.
5. Conta quantas vezes cada IP aparece.
6. Mostra os IPs que mais tentaram atacar o servidor.

---

## 🧠 Tecnologias usadas

- Python 3
- `re` (expressões regulares)
- `collections.Counter`

---

---

## 📍 Código completo

```python
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

# Imprimir resultado
print("IPs atacantes:")
for ip, quantidade in contagem.items():
    print(f"{ip} → {quantidade}")

## 📄 Exemplo de Saída

