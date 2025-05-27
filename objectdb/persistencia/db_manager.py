# Gerencia conexão e operações CRUD no ObjectDB (ZODB)
import transaction
from ZODB import FileStorage, DB

class DBManager:
    def __init__(self, path='data.fs'):
        """
        Inicializa a conexão com o banco ObjectDB.
        
        Args:
            path (str): Caminho para o arquivo de armazenamento do ZODB.
        """
        storage = FileStorage.FileStorage(path)
        self.db = DB(storage)  # Cria o banco de dados
        self.connection = self.db.open()  # Abre uma conexão
        self.root = self.connection.root()  # Obtém o objeto raiz do banco

    def close(self):
        """
        Fecha a conexão e o banco.
        """
        self.connection.close()
        self.db.close()

    def add_obj(self, key, obj):
        """
        Adiciona um objeto no banco sob uma chave específica.
        
        Args:
            key (str): Chave identificadora do objeto.
            obj: Objeto a ser armazenado.
        """
        self.root[key] = obj
        transaction.commit()  # Salva a transação

    def get_obj(self, key):
        """
        Recupera um objeto pelo identificador chave.
        
        Args:
            key (str): Chave do objeto a recuperar.
        
        Returns:
            O objeto armazenado, ou None se não encontrado.
        """
        return self.root.get(key)

    def delete_obj(self, key):
        """
        Remove um objeto do banco pelo identificador chave.
        
        Args:
            key (str): Chave do objeto a ser removido.
        """
        if key in self.root:
            del self.root[key]
            transaction.commit()

    def update_obj(self, key, new_obj):
        """
        Atualiza o objeto existente no banco.
        
        Args:
            key (str): Chave do objeto a atualizar.
            new_obj: Novo objeto para substituir o antigo.
        """
        if key in self.root:
            self.root[key] = new_obj
            transaction.commit()