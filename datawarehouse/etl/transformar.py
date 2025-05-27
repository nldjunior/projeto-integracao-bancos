import pandas as pd

def transformar_produtos(df_produtos):
    """
    Realiza a transformação dos dados de produtos para o formato do Data Warehouse.
    - Renomeia coluna 'id' para 'id_produto' se necessário.
    - Remove duplicatas com base no 'id_produto'.
    - Renomeia coluna 'nome' para 'nome_produto' se existir.
    - Seleciona as colunas relevantes para o DW.
    """
    if 'id' in df_produtos.columns and 'id_produto' not in df_produtos.columns:
        df_produtos = df_produtos.rename(columns={'id': 'id_produto'})
    df = df_produtos.drop_duplicates(subset=['id_produto'])
    if 'nome' in df.columns:
        df = df.rename(columns={'nome': 'nome_produto'})
    colunas = [col for col in ['id_produto', 'nome_produto', 'categoria'] if col in df.columns]
    return df[colunas]

def transformar_clientes(df_clientes):
    """
    Realiza a transformação dos dados de clientes para o formato do Data Warehouse.
    - Renomeia coluna 'id' para 'id_cliente' se necessário.
    - Remove duplicatas com base em 'id_cliente'.
    - Cria a faixa etária com base na idade (bins).
    - Seleciona as colunas relevantes para o DW.
    """
    if 'id' in df_clientes.columns and 'id_cliente' not in df_clientes.columns:
        df_clientes = df_clientes.rename(columns={'id': 'id_cliente'})
    df = df_clientes.drop_duplicates(subset=['id_cliente'])
    if 'idade' in df.columns:
        bins = [0, 18, 35, 60, 120]
        labels = ['0-17', '18-34', '35-59', '60+']
        df['faixa_etaria'] = pd.cut(df['idade'], bins=bins, labels=labels, right=False)
    else:
        df['faixa_etaria'] = 'Desconhecida'
    colunas = [col for col in ['id_cliente', 'nome', 'sexo', 'faixa_etaria', 'cidade', 'estado', 'regiao'] if col in df.columns]
    return df[colunas]

def transformar_localidades(df_localidades):
    """
    Prepara a dimensão localidades:
    - Remove duplicatas.
    - Cria um identificador único 'id_localidade'.
    - Seleciona as colunas relevantes para o DW.
    """
    df = df_localidades.drop_duplicates().reset_index(drop=True)
    df['id_localidade'] = df.index + 1
    colunas = [col for col in ['id_localidade', 'cidade', 'estado', 'regiao'] if col in df.columns]
    return df[colunas]

def transformar_tempo(df_tempo):
    """
    Prepara a dimensão tempo:
    - Remove duplicatas baseadas na data.
    - Cria um identificador único 'id_tempo'.
    - Seleciona as colunas relevantes para o DW.
    """
    df = df_tempo.drop_duplicates(subset=['data']).reset_index(drop=True)
    df['id_tempo'] = df.index + 1
    colunas = [col for col in ['id_tempo', 'data', 'dia', 'mes', 'trimestre', 'ano', 'dia_semana'] if col in df.columns]
    return df[colunas]

def transformar_vendas(df_vendas, df_tempo, df_produtos, df_clientes, df_localidades):
    """
    Prepara a tabela fato vendas:
    - Converte a coluna 'data' para datetime.
    - Mapeia os IDs das dimensões tempo, produto, cliente e localidade para a tabela fato.
    - Faz o merge para associar 'id_localidade' via cliente e localidades.
    - Seleciona as colunas de medidas e chaves estrangeiras para o DW.
    """
    df_vendas['data'] = pd.to_datetime(df_vendas['data'])

    # Mapear id_tempo a partir da dimensão tempo
    df_tempo_map = df_tempo.set_index('data')['id_tempo']
    df_vendas['id_tempo'] = df_vendas['data'].map(df_tempo_map)

    # Mapear id_produto
    if 'produto_id' in df_vendas.columns:
        df_vendas['id_produto'] = df_vendas['produto_id']
    elif 'id_produto' in df_vendas.columns:
        pass
    else:
        raise KeyError("Coluna 'produto_id' ou 'id_produto' não encontrada em vendas")

    # Mapear id_cliente
    if 'cliente_id' in df_vendas.columns:
        df_vendas['id_cliente'] = df_vendas['cliente_id']
    elif 'id_cliente' in df_vendas.columns:
        pass
    else:
        raise KeyError("Coluna 'cliente_id' ou 'id_cliente' não encontrada em vendas")

    # Mapear id_localidade via merge entre clientes e localidades
    df_clientes = df_clientes.merge(df_localidades, on=['cidade', 'estado', 'regiao'], how='left')
    df_vendas = df_vendas.merge(df_clientes[['id_cliente', 'id_localidade']], on='id_cliente', how='left')

    colunas = ['id_tempo', 'id_produto', 'id_cliente', 'id_localidade', 'quantidade', 'valor_total', 'desconto']
    colunas_existentes = [c for c in colunas if c in df_vendas.columns]
    df_fato = df_vendas[colunas_existentes]

    return df_fato