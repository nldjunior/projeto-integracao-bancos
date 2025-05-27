from sqlalchemy import text

def carregar_dimensao(df, tabela, engine):
    """
    Carrega dados em uma tabela dimensão do Data Warehouse no PostgreSQL.

    Parâmetros:
    - df: DataFrame contendo os dados a serem carregados.
    - tabela: Nome da tabela de destino (ex: 'dim_cliente', 'dim_produto', etc.).
    - engine: Conexão SQLAlchemy com o banco PostgreSQL.
    """

    # Seleciona colunas válidas de acordo com a dimensão
    if tabela == 'dim_cliente':
        colunas_validas = [col for col in ['nome', 'sexo', 'faixa_etaria', 'cidade'] if col in df.columns]
        df = df[colunas_validas]

    elif tabela == 'dim_produto':
        # Renomeia coluna caso necessário
        if 'nome_produto' in df.columns:
            df = df.rename(columns={'nome_produto': 'nome'})
        colunas_validas = [col for col in ['nome', 'categoria'] if col in df.columns]
        df = df[colunas_validas]

    elif tabela == 'dim_localidade':
        colunas_validas = [col for col in ['cidade', 'estado', 'regiao'] if col in df.columns]
        df = df[colunas_validas]

    elif tabela == 'dim_tempo':
        colunas_validas = [col for col in ['data', 'dia', 'mes', 'trimestre', 'ano', 'dia_semana'] if col in df.columns]
        df = df[colunas_validas]

    # Trunca a tabela para evitar dados duplicados e reinicia o ID
    with engine.begin() as conn:
        conn.execute(text(f'TRUNCATE TABLE {tabela} RESTART IDENTITY CASCADE;'))
        df.to_sql(tabela, con=conn, if_exists='append', index=False)

    print(f'Tabela {tabela} carregada com {len(df)} registros.')

def carregar_fato(df_fato, engine):
    """
    Carrega dados na tabela fato do Data Warehouse (fato_vendas).

    Parâmetros:
    - df_fato: DataFrame com os dados de vendas agregados.
    - engine: Conexão SQLAlchemy com o banco PostgreSQL.
    """

    # Trunca a tabela fato para evitar duplicação
    with engine.begin() as conn:
        conn.execute(text('TRUNCATE TABLE fato_vendas RESTART IDENTITY CASCADE;'))
        df_fato.to_sql('fato_vendas', con=conn, if_exists='append', index=False)

    print(f'Tabela fato_vendas carregada com {len(df_fato)} registros.')