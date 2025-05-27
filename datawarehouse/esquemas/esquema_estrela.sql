-- dimensão tempo
CREATE TABLE dim_tempo (
    id_tempo SERIAL PRIMARY KEY,
    data DATE NOT NULL,
    dia INT NOT NULL,
    mes INT NOT NULL,
    trimestre INT NOT NULL,
    ano INT NOT NULL,
    dia_semana INT NOT NULL
);

-- dimensão produto
CREATE TABLE dim_produto (
    id_produto SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    categoria VARCHAR(100) NOT NULL
);

-- dimensão cliente
CREATE TABLE dim_cliente (
    id_cliente SERIAL PRIMARY KEY,
    nome VARCHAR(255),
    sexo VARCHAR(10),
    faixa_etaria VARCHAR(20),
    cidade VARCHAR(100)
);

-- dimensão localidade
CREATE TABLE dim_localidade (
    id_localidade SERIAL PRIMARY KEY,
    cidade VARCHAR(100),
    estado VARCHAR(100),
    regiao VARCHAR(100)
);

-- tabela Fato Vendas
CREATE TABLE fato_vendas (
    id_fato SERIAL PRIMARY KEY,
    id_tempo INT NOT NULL REFERENCES dim_tempo(id_tempo),
    id_produto INT NOT NULL REFERENCES dim_produto(id_produto),
    id_cliente INT NOT NULL REFERENCES dim_cliente(id_cliente),
    id_localidade INT NOT NULL REFERENCES dim_localidade(id_localidade),
    quantidade INT NOT NULL,
    valor_total DECIMAL(10, 2) NOT NULL,
    desconto DECIMAL(10, 2) DEFAULT 0
);