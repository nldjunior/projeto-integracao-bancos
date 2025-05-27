from pymongo import MongoClient
from pprint import pprint

# Conexão com o servidor MongoDB local
client = MongoClient("mongodb://localhost:27017/")

# Acesso ao banco de dados 'vendasDB'
db = client["vendasDB"]
# Referências às coleções de vendas e comentários
colecao_vendas = db["vendas"]
colecao_comentarios = db["comentarios"]

# --- Consultas na coleção 'vendas' ---

def consulta_total_vendas_por_cliente():
    print("\n📌 Total de vendas por cliente:")
    resultado = colecao_vendas.aggregate([
        {
            "$group": {
                "_id": "$cliente.nome",
                "total_vendas": {"$sum": "$valor_total"}
            }
        },
        {"$sort": {"total_vendas": -1}}
    ])
    for doc in resultado:
        pprint(doc)

def consulta_quantidade_por_produto():
    print("\n📌 Quantidade total vendida por produto:")
    resultado = colecao_vendas.aggregate([
        {
            "$group": {
                "_id": "$produto.nome",
                "quantidade_total": {"$sum": "$quantidade"}
            }
        }
    ])
    for doc in resultado:
        pprint(doc)

def consulta_vendas_por_regiao():
    print("\n📌 Total de vendas por região:")
    resultado = colecao_vendas.aggregate([
        {
            "$group": {
                "_id": "$cliente.regiao",
                "total_vendas": {"$sum": "$valor_total"}
            }
        }
    ])
    for doc in resultado:
        pprint(doc)

def consulta_comentarios_positivos():
    print("\n🟢 Comentários positivos (avaliação >= 4):")
    resultado = colecao_comentarios.find({"avaliacao": {"$gte": 4}})
    for doc in resultado:
        pprint(doc)

# --- Função principal que executa apenas as consultas que funcionam ---
def main():
    consulta_total_vendas_por_cliente()
    consulta_quantidade_por_produto()
    consulta_vendas_por_regiao()
    consulta_comentarios_positivos()

if __name__ == "__main__":
    main()