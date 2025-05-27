import os
from sqlalchemy import create_engine

from extrair import (
    extrair_produtos,
    extrair_clientes,
    extrair_vendas,
    extrair_localidades,
    extrair_tempo
)
from transformar import (
    transformar_produtos,
    transformar_clientes,
    transformar_localidades,
    transformar_tempo,
    transformar_vendas
)
from carregar import carregar_dimensao, carregar_fato

# Define o diretório base do projeto e o caminho para a pasta de dados
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
CAMINHO_DADOS = os.path.join(BASE_DIR, 'dados')

def verificar_arquivo(caminho_arquivo):
    """
    Verifica se um arquivo existe no caminho especificado.
    Lança uma exceção se o arquivo não for encontrado.

    Parâmetros:
    - caminho_arquivo: caminho absoluto do arquivo a ser verificado
    """
    if not os.path.isfile(caminho_arquivo):
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho_arquivo}")

def run_etl():
    """
    Executa o pipeline ETL completo:
    - Extrai os dados dos arquivos CSV
    - Transforma os dados para os formatos esperados
    - Carrega os dados no PostgreSQL conforme o modelo estrela
    """
    print('Iniciando ETL...')

    # Define os caminhos para os arquivos de entrada
    arquivo_produtos = os.path.join(CAMINHO_DADOS, 'produtos.csv')
    arquivo_clientes = os.path.join(CAMINHO_DADOS, 'clientes.csv')
    arquivo_vendas = os.path.join(CAMINHO_DADOS, 'vendas.csv')

    # Valida a existência dos arquivos
    verificar_arquivo(arquivo_produtos)
    verificar_arquivo(arquivo_clientes)
    verificar_arquivo(arquivo_vendas)

    # Extração dos dados
    print(f"Lendo arquivo produtos em: {arquivo_produtos}")
    produtos = extrair_produtos(arquivo_produtos)

    print(f"Lendo arquivo clientes em: {arquivo_clientes}")
    clientes = extrair_clientes(arquivo_clientes)

    print("Extraindo localidades a partir dos clientes")
    localidades = extrair_localidades(clientes)

    print(f"Lendo arquivo vendas em: {arquivo_vendas}")
    vendas = extrair_vendas(arquivo_vendas)

    print("Extraindo dimensão tempo a partir das vendas")
    tempo = extrair_tempo(vendas)

    print('Extração concluída')

    # Transformação dos dados em dimensões e fato
    dim_produtos = transformar_produtos(produtos)
    dim_clientes = transformar_clientes(clientes)
    dim_localidades = transformar_localidades(localidades)
    dim_tempo = transformar_tempo(tempo)
    fato_vendas = transformar_vendas(vendas, dim_tempo, dim_produtos, dim_clientes, dim_localidades)

    print('Transformação concluída')

    # Criação da engine de conexão com o PostgreSQL
    engine = create_engine('postgresql+psycopg2://postgres:juniorteste123@localhost:5432/projetodb')

    # Carga dos dados nas tabelas do Data Warehouse
    carregar_dimensao(dim_produtos, 'dim_produto', engine)
    carregar_dimensao(dim_clientes, 'dim_cliente', engine)
    carregar_dimensao(dim_localidades, 'dim_localidade', engine)
    carregar_dimensao(dim_tempo, 'dim_tempo', engine)
    carregar_fato(fato_vendas, engine)

    print('Carga concluída')
    print('ETL finalizado com sucesso!')

# Permite que o script seja executado diretamente
if __name__ == '__main__':
    run_etl()