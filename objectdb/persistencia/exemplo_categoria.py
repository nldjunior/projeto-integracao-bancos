from objectdb.modelos.categoria import Categoria
from objectdb.persistencia.db_manager import DBManager

def main():
    db = DBManager()  # Inicializa o gerenciador de banco ObjectDB (arquivo padrão data.fs)

    categoria = Categoria(1, 'Material Escolar')  # Cria uma instância da classe Categoria
    db.add_obj('categoria_1', categoria)  # Adiciona a categoria no banco com chave 'categoria_1'

    c = db.get_obj('categoria_1')  # Recupera a categoria pelo id/chave
    print('Categoria inserida:', c)  # Imprime o objeto recuperado

    # Atualizar nome da categoria
    categoria.nome = 'Papelaria'  # Modifica o atributo nome do objeto
    db.update_obj('categoria_1', categoria)  # Atualiza o objeto no banco
    print('Categoria atualizada:', db.get_obj('categoria_1'))  # Imprime a versão atualizada

    # Deletar categoria
    db.delete_obj('categoria_1')  # Remove o objeto da base
    print('Categoria deletada:', db.get_obj('categoria_1'))  # Tenta recuperar, deve retornar None

    db.close()  # Fecha conexão com o banco

if __name__ == '__main__':
    main()