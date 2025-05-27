from objectdb.modelos.produto import Produto
from objectdb.persistencia.db_manager import DBManager

def main():
    db = DBManager()  # Abre conexão com o banco

    # Cria o objeto Produto com: id, nome, preco, estoque, categoria e fornecedor
    produto = Produto(1, 'Caneta', 2.5, 100, 'Material Escolar', 'Fornecedor X')

    db.add_obj('produto_1', produto)  # Insere o produto no banco com a chave 'produto_1'

    p = db.get_obj('produto_1')  # Busca o produto no banco
    print(p)  # Exibe o produto (usa __repr__)

    db.close()  # Fecha a conexão

if __name__ == '__main__':
    main()