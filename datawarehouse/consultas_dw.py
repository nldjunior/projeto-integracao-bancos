from sqlalchemy import create_engine, text

# Cria a engine de conexão com o banco PostgreSQL
engine = create_engine('postgresql+psycopg2://postgres:juniorteste123@localhost:5432/projetodb')

def executar_consulta(sql, descricao):
    """
    Executa uma consulta SQL no banco PostgreSQL usando SQLAlchemy.
    
    Parâmetros:
    - sql: string contendo o comando SQL a ser executado.
    - descricao: texto descritivo para impressão antes dos resultados.
    
    Imprime o resultado formatado no console.
    """
    with engine.connect() as conn:
        resultado = conn.execute(text(sql))
        print(f"\n📌 {descricao}")
        for row in resultado:
            print(f"Categoria: {row.categoria}, Total de Vendas: {row.total_vendas}")

def main():
    """
    Define a consulta de vendas por categoria de produto e chama a execução.
    """
    consulta = """
    SELECT p.categoria, SUM(f.valor_total) AS total_vendas
    FROM fato_vendas f
    JOIN dim_produto p ON f.id_produto = p.id_produto
    GROUP BY p.categoria;
    """
    executar_consulta(consulta, "Total de vendas por categoria de produto:")

if __name__ == "__main__":
    main()