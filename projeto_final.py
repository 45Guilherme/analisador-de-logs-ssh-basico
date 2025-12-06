import re

with open("server.log" , "w") as arquivo:
    arquivo.write("Nov 12 14:33:01 server sshd[1201]: Failed password for root from 177.233.10.45 port 45821 ssh2\n")
    arquivo.write("Nov 12 14:34:17 server sshd[1202]: Failed password for invalid user admin from 201.55.18.10 port 51200 ssh2\n")
    arquivo.write("Nov 12 14:35:40 server sshd[1203]: Failed password for ubuntu from 185.12.245.90 port 60214 ssh2\n")
    arquivo.write("Nov 12 14:36:22 server sshd[1204]: Failed password for root from 3.3.3.3 port 44412 ssh2\n")
    arquivo.write("Nov 12 14:37:58 server sshd[1205]: Failed password for test from 1.1.1.1 port 60123 ssh2\n")
    arquivo.write("Nov 12 14:38:30 server sshd[1206]: Accepted password for gui from 192.168.0.10 port 55022 ssh2\n")
    arquivo.write("Nov 12 14:38:41 server systemd[1]: Started Daily apt download activities.\n")
    arquivo.write("Nov 12 14:38:41 server systemd[1]: Started Daily apt download activities.\n")
    arquivo.write("Nov 12 14:39:05 server sshd[1207]: Connection closed by 192.168.0.12 port 55110 ssh2\n")
    arquivo.write("Nov 12 14:39:40 server CRON[1208]: (root) CMD (backup.sh)\n")
    arquivo.write("Nov 12 14:40:15 server sshd[1209]: Accepted password for maria from 192.168.0.22 port 55221 ssh2\n")

with open("server.log", "r") as arquivo:
    linhas = arquivo.readlines()
    print(f"{linhas}\n")

    for linha in linhas:
        if "Failed password" in linha:
            print(linha)
    for linha in linhas:
        if "Failed password" in linha:
            regex = r"from ([\d\.]+) port"
            achou = re.search(regex, linha)
            print(achou.group(1))
           
           
        
        















