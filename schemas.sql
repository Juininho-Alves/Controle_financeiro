-- Criar uma tabela para determinar uma meta 
-- Criar uma tabela para os valores ganho no dia
-- Criar uma tabela para gastos


CREATE TABLE movimentacoes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tipo TEXT,
    motivo TEXT,
    dia TEXT,
    valor DECIMAL
);