from persistent import Persistent

# Classe Categoria que herda de Persistent para persistência de dados
class Categoria(Persistent):
    def __init__(self, id, nome, descricao=None):
        # Identificador único da categoria
        self.id = id
        # Nome da categoria
        self.nome = nome
        # Descrição opcional da categoria
        self.descricao = descricao

    def __repr__(self):
        # Representação legível da instância da classe para depuração e exibição
        return f"Categoria(id={self.id}, nome={self.nome})"