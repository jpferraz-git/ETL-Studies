from _datetime import datetime
import json

from typing import *

json_data = [
    { "nome": "Biscoito Teens",
      "preco": 3.50,
      "marca": "Nestle",
      "tipo": "Alimento",
      "validade": "2025-08-01"
    },
  {
    "nome": "Leite Integral",
    "preco": 4.99,
    "marca": "Lactomil",
    "tipo": "Bebida alcoólica",
    "validade": "2025-07-10"
  },
  {
    "nome": "Sabonete de Lavanda",
    "preco": 2.50,
    "marca": "Floralis",
    "tipo": "Alimento",
    "validade": None
  },
  {
    "nome": "Iogurte Natural",
    "preco": 3.20,
    "marca": "VidaLeve",
    "tipo": "Laticínio",
    "validade": "2024-05-01"
  },
  {
    "nome": "Cerveja Pilsen",
    "preco": 1.50,
    "marca": "Brauhaus",
    "tipo": "Refrigerante",
    "validade": "2025-09-15"
  },
  {
    "nome": "Arroz Branco 5kg",
    "preco": -10.00,
    "marca": "BomSabor",
    "tipo": "Grão",
    "validade": "2026-01-01"
  },
  {
    "nome": "Detergente Líquido",
    "preco": 3.75,
    "marca": "LimpezaJá",
    "tipo": "Produto de Limpeza",
    "validade": "2023-12-31"
  },
  {
    "nome": "Banana Prata (kg)",
    "preco": 7.90,
    "marca": "Frutas do Vale",
    "tipo": "Fruta",
    "validade": "2025-06-26"
  },
  {
    "nome": "Biscoito de Chocolate",
    "preco": 5.00,
    "marca": "ChocoBite",
    "tipo": "Produto de Higiene",
    "validade": "2025-03-01"
  },
  {
    "nome": "Presunto Fatiado",
    "preco": 6.75,
    "marca": "SaborSul",
    "tipo": "Embutido",
    "validade": "2024-06-01"
  },
  {
    "nome": "Café Torrado e Moído",
    "preco": 12.90,
    "marca": "Café Bom Dia",
    "tipo": "Perecível",
    "validade": None
  }
]

def treating_data(data: List[Dict[str, Any]]) -> None:
    for values in data:
        for key, value in values.items():
          if key == "preco":
            if value < 0.0:
              print("Preco Negativo, invalido")
            else:
              print(f"Preco: {value}")

          if key == "validade":
            if value is not None:
              # validade_formatada = lambda x: datetime.strptime(x, "%Y-%m-%d").date()
              validade_formatada = datetime.strptime(value, "%Y-%m-%d").date()
              if validade_formatada < datetime.strptime("2025-07-01", "%Y-%m-%d").date():
                print(f"Produto vencido: {validade_formatada}")
              else:
                print(validade_formatada)
            else:
              print("Date is Null")

def json_writer(data):

    treating_data(data)
    path = "/home/user/ETL-Studies/ETL-Studies/data_cleaning_script/repository/items.json"

    with open(path, "w") as file:
        json.dump(data, file, indent=4)


# json_writer(json_data)
treating_data(json_data)