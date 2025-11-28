import re

texto = "Failed password for root from 185.234.55.1 port 39302 ssh2"

padrao = r"Failed password for root from ([\d\.]+) port 39302 ssh2"

resultado = re.search(padrao, texto)