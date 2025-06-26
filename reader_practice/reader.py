import json
file_path = "/home/user/Documentos/arquivosGravados/Configuracoes/Configuracoes Gerais/Bancos.json"
try:
    with open(file_path, "r") as file:
        content = json.load(file, end= "\n")
        print(content)
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Cannot read that file")