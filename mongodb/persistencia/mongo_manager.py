from pymongo import MongoClient
from datetime import datetime

# Conexão com o servidor MongoDB local
client = MongoClient("mongodb://localhost:27017/")

# Acesso ao banco de dados 'projetodb'
db = client["projetodb"]

# Referência à coleção 'comentarios'
colecao = db["comentarios"]

def inserir_comentario(cliente_id, produto, avaliacao, comentario):
    """
    Insere um novo documento na coleção 'comentarios' com os dados fornecidos,
    incluindo a data/hora atual da inserção.
    Parâmetros:
        cliente_id (str/int): Identificador do cliente que fez o comentário
        produto (str): Nome ou código do produto comentado
        avaliacao (int): Avaliação numérica (ex: 1 a 5)
        comentario (str): Texto do comentário
    """
    documento = {
        "cliente_id": cliente_id,
        "produto": produto,
        "avaliacao": avaliacao,
        "comentario": comentario,
        "data": datetime.now()
    }
    colecao.insert_one(documento)
    print("Comentário inserido com sucesso!")

def listar_comentarios_positivos():
    """
    Busca e exibe todos os comentários com avaliação maior ou igual a 4.
    """
    for doc in colecao.find({"avaliacao": {"$gte": 4}}):
        print(doc)

# Teste rápido: lista comentários positivos ao executar o script diretamente
if __name__ == "__main__":
    listar_comentarios_positivos()