from pymongo import MongoClient
from datetime import datetime

# Conexão com o MongoDB local
client = MongoClient("mongodb://localhost:27017/")

# Acesso ao banco de dados 'projetodb'
db = client["projetodb"]  # Pode trocar o nome se estiver usando outro

# Referência à coleção 'comentarios'
comentarios = db["comentarios"]

# Dados de exemplo: lista de documentos contendo comentários dos clientes sobre produtos
dados = [
    {
        "cliente_id": "C001",
        "produto": "Caneta Azul",
        "avaliacao": 5,
        "comentario": "Ótima qualidade, muito boa!",
        "data": datetime(2024, 5, 1)
    },
    {
        "cliente_id": "C002",
        "produto": "Lápis Preto",
        "avaliacao": 3,
        "comentario": "Cumpre o básico, mas quebra fácil.",
        "data": datetime(2024, 5, 2)
    },
    {
        "cliente_id": "C003",
        "produto": "Caderno Espiral",
        "avaliacao": 4,
        "comentario": "Muito bom, resistente e barato.",
        "data": datetime(2024, 5, 3)
    }
]

# Inserção dos documentos na coleção 'comentarios'
comentarios.insert_many(dados)
print("✅ Comentários inseridos com sucesso.")
