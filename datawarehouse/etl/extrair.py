import pandas as pd

def extrair_produtos(caminho):
    """
    Extrai os dados de produtos a partir de um arquivo CSV.

    Parâmetros:
    - caminho: Caminho para o arquivo CSV.

    Retorna:
    - DataFrame com os dados dos produtos.
    """
    return pd.read_csv(caminho)

def extrair_clientes(caminho):
    """
    Extrai os dados de clientes a partir de um arquivo CSV.

    Parâmetros:
    - caminho: Caminho para o arquivo CSV.

    Retorna:
    - DataFrame com os dados dos clientes.
    """
    return pd.read_csv(caminho)

def extrair_localidades(df_clientes):
    """
    Extrai e remove duplicatas das colunas de localidade (cidade, estado, região) dos clientes.

    Parâmetros:
    - df_clientes: DataFrame com os dados dos clientes.

    Retorna:
    - DataFrame com localizações únicas (cidade, estado, região).
    """
    colunas = [col for col in ['cidade', 'estado', 'regiao'] if col in df_clientes.columns]
    return df_clientes[colunas].drop_duplicates()

def extrair_vendas(caminho):
    """
    Extrai os dados de vendas a partir de um arquivo CSV.

    Parâmetros:
    - caminho: Caminho para o arquivo CSV.

    Retorna:
    - DataFrame com os dados das vendas.
    """
    return pd.read_csv(caminho)

def extrair_tempo(df_vendas):
    """
    Constrói a dimensão de tempo a partir da coluna de datas do DataFrame de vendas.

    Parâmetros:
    - df_vendas: DataFrame com os dados das vendas (deve conter a coluna 'data').

    Retorna:
    - DataFrame com colunas derivadas da data: dia, mês, trimestre, ano e dia da semana.
    """
    df_tempo = pd.DataFrame()
    df_tempo['data'] = pd.to_datetime(df_vendas['data'])
    df_tempo['dia'] = df_tempo['data'].dt.day
    df_tempo['mes'] = df_tempo['data'].dt.month
    df_tempo['trimestre'] = df_tempo['data'].dt.quarter
    df_tempo['ano'] = df_tempo['data'].dt.year
    df_tempo['dia_semana'] = df_tempo['data'].dt.weekday + 1  # Segunda=1, Domingo=7
    return df_tempo.drop_duplicates()