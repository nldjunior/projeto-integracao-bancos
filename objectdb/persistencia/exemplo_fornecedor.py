from objectdb.modelos.fornecedor import Fornecedor
from objectdb.persistencia.db_manager import DBManager

def main():
    db = DBManager()  # Inicializa o gerenciador do banco (abre conexão com data.fs)

    fornecedor = Fornecedor(1, 'Fornecedor X')  # Cria uma instância de Fornecedor
    db.add_obj('fornecedor_1', fornecedor)  # Insere o fornecedor no banco com a chave 'fornecedor_1'

    f = db.get_obj('fornecedor_1')  # Recupera o fornecedor do banco
    print('Fornecedor inserido:', f)  # Imprime o fornecedor recuperado

    # Atualizar nome do fornecedor
    fornecedor.nome = 'Fornecedor Y'  # Altera o nome do objeto em memória
    db.update_obj('fornecedor_1', fornecedor)  # Atualiza o objeto no banco
    print('Fornecedor atualizado:', db.get_obj('fornecedor_1'))  # Imprime a versão atualizada do fornecedor

    # Deletar fornecedor
    db.delete_obj('fornecedor_1')  # Remove o fornecedor do banco
    print('Fornecedor deletado:', db.get_obj('fornecedor_1'))  # Tenta recuperar, deve retornar None

    db.close()  # Fecha conexão com o banco

if __name__ == '__main__':
    main()