-- Criar uma tabela para determinar uma meta 
-- Criar uma tabela para os valores ganho no dia
-- Criar uma tabela para gastos

CREATE TABLE meta (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    valor_meta DECIMAL
);

CREATE TABLE lucro (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    valor_lucro DECIMAL,
    dia TEXT
);

CREATE TABLE despesas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    valor_despesas DECIMAL,
    nome_despesa TEXT
);