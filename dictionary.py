pessoa = {
    "nome": "João",
    "idade": 30,
    "cidade": "São Paulo"
}

for key, value in pessoa.items():
    if key == "nome":
        print(key, value)

profissao = {"profissao": "engenheiro"}

pessoa.update(profissao)

print(pessoa)

cidade_removidade = "cidade"

pessoa.pop(cidade_removidade)

print(pessoa)

frase = "o rato roeu a roupa do rei de roma"

novo_dicionario = {}

for palavra in range(len(frase)):
    if frase[palavra] == " ":
        contador_palavra = len(frase[palavra]) -
        novo_dicionario.update()