from persistent import Persistent

# Classe Fornecedor que herda de Persistent para armazenamento persistente
class Fornecedor(Persistent):
    def __init__(self, id, nome, cnpj=None, email=None, telefone=None):
        # Identificador único do fornecedor
        self.id = id
        # Nome do fornecedor
        self.nome = nome
        # CNPJ do fornecedor (opcional)
        self.cnpj = cnpj
        # E-mail do fornecedor (opcional)
        self.email = email
        # Telefone do fornecedor (opcional)
        self.telefone = telefone

    def __repr__(self):
        # Representação legível para facilitar depuração e exibição
        return f"Fornecedor(id={self.id}, nome={self.nome})"