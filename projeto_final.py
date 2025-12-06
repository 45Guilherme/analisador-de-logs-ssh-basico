import re  # Importa o módulo 're' para trabalhar com expressões regulares

     
with open("server.log", "w") as file:
          file.write("Nov 12 14:33:01 server sshd[1201]: Failed password for root from 177.233.10.45 port 45821 ssh2\n")
          file.write("Nov 12 14:34:17 server sshd[1202]: Failed password for invalid user admin from 201.55.18.10 port 51200 ssh2\n")
          file.write("Nov 12 14:35:40 server sshd[1203]: Failed password for ubuntu from 185.12.245.90 port 60214 ssh2\n")
          file.write("Nov 12 14:36:22 server sshd[1204]: Failed password for root from 3.3.3.3 port 44412 ssh2\n")
          file.write("Nov 12 14:37:58 server sshd[1205]: Failed password for test from 1.1.1.1 port 60123 ssh2\n")
          file.write("Nov 12 14:38:30 server sshd[1206]: Accepted password for gui from 192.168.0.10 port 55022 ssh2\n")
          file.write("Nov 12 14:38:41 server systemd[1]: Started Daily apt download activities.\n")
          file.write("Nov 12 14:38:41 server systemd[1]: Started Daily apt download activities.\n")
          file.write("Nov 12 14:39:05 server sshd[1207]: Connection closed by 192.168.0.12 port 55110 ssh2\n")
          file.write("Nov 12 14:39:40 server CRON[1208]: (root) CMD (backup.sh)\n")
          file.write("Nov 12 14:40:15 server sshd[1209]: Accepted password for maria from 192.168.0.22 port 55221 ssh2\n")
# ---------------------------------------------------------
# 2) Leitura do arquivo de log e exibição das linhas
# ---------------------------------------------------------
with open("server.log", "r") as arquivo:
    linhas = arquivo.readlines()

# Mostra todas as linhas do log (apenas para debug)
print(f"{linhas}\n")

# ---------------------------------------------------------
# 3) Filtrando apenas tentativas de login falhas (Failed password)
# ---------------------------------------------------------
print("Linhas com tentativas de ataque:\n")
def realizando_analise(linhas):

    ataques = {}
    maior_ip = None
    maior_qtd = 0
    regex = r"from ([\d\.]+) port"   # define apenas 1 vez

    for linha in linhas:

        if "Failed password" in linha:         
            match = re.search(regex, linha)

            if match:
                ip = match.group(1)

                if ip in ataques:
                    ataques[ip] += 1
                else:
                    ataques[ip] = 1

                print(ip)  # exibe apenas IPs válidos

    # ---- Encontrar o IP com mais ataques ----
    for ip, qtd in ataques.items():
        if qtd > maior_qtd:
            maior_qtd = qtd
            maior_ip = ip

    print("\nIP que mais atacou:", maior_ip, "com", maior_qtd, "tentativas")




