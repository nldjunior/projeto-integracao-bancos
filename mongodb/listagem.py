from pymongo import MongoClient

# Conexão com o servidor MongoDB local
client = MongoClient("mongodb://localhost:27017/")

# Acessa o banco de dados 'projetodb'
db = client["projetodb"]

# Lista e imprime os nomes das coleções presentes no banco de dados
print(db.list_collection_names())