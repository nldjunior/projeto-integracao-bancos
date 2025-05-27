from persistent import Persistent

# Classe Produto que herda de Persistent para armazenamento persistente
class Produto(Persistent):
    def __init__(self, id, nome, preco, estoque, categoria, fornecedor):
        # Identificador único do produto
        self.id = id
        # Nome do produto
        self.nome = nome
        # Preço unitário do produto
        self.preco = preco
        # Quantidade em estoque do produto
        self.estoque = estoque
        # Categoria do produto (objeto ou referência)
        self.categoria = categoria
        # Fornecedor do produto (objeto ou referência)
        self.fornecedor = fornecedor

    def __repr__(self):
        # Representação legível para facilitar depuração e exibição
        return f"Produto(id={self.id}, nome={self.nome}, preco={self.preco}, estoque={self.estoque})"