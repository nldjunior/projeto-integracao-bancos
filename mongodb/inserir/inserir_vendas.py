from pymongo import MongoClient

# Conectar ao MongoDB local
client = MongoClient("mongodb://localhost:27017/")

# Selecionar o banco de dados 'vendasDB'
db = client["vendasDB"]

# Selecionar a coleção 'vendas'
vendas = db["vendas"]

# Lista de documentos representando registros de vendas
dados = [
    {
        "cliente": {
            "nome": "Ana",
            "regiao": "Sudeste"
        },
        "produto": {
            "nome": "Caneta Azul"
        },
        "quantidade": 10,
        "valor_total": 25.00
    },
    {
        "cliente": {
            "nome": "Carlos",
            "regiao": "Sul"
        },
        "produto": {
            "nome": "Lápis Preto"
        },
        "quantidade": 20,
        "valor_total": 40.00
    },
    {
        "cliente": {
            "nome": "Ana",
            "regiao": "Sudeste"
        },
        "produto": {
            "nome": "Caderno Espiral"
        },
        "quantidade": 5,
        "valor_total": 50.00
    }
]

# Inserir os documentos na coleção 'vendas'
vendas.insert_many(dados)

print("✅ Vendas inseridas com sucesso.")