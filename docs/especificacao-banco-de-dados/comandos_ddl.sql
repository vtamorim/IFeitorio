CREATE TABLE IF NOT EXISTS alunos (
    matricula TEXT PRIMARY KEY NOT NULL,
    nome TEXT NOT NULL,
    senha TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS restricoes_alimentares (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS aluno_restricao (
    aluno_matricula TEXT NOT NULL,
    restricao_id INTEGER NOT NULL,
    FOREIGN KEY (aluno_matricula)
        REFERENCES alunos (matricula)
        ON DELETE CASCADE,
    FOREIGN KEY (restricao_id)
        REFERENCES restricoes_alimentares (id)
        ON DELETE CASCADE,
    PRIMARY KEY (aluno_matricula, restricao_id)
);
CREATE TABLE IF NOT EXISTS coordenadores (
    matricula TEXT PRIMARY KEY NOT NULL,
    nome TEXT NOT NULL,
    senha TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS refeicoes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    descricao TEXT
);
CREATE TABLE IF NOT EXISTS refeicao_restricao_alimentar (
    refeicao_id INTEGER NOT NULL,
    restricao_id INTEGER NOT NULL,
    FOREIGN KEY (refeicao_id)
        REFERENCES refeicoes (id)
        ON DELETE CASCADE,
    FOREIGN KEY (restricao_id)
        REFERENCES restricoes_alimentares (id)
        ON DELETE CASCADE,
    PRIMARY KEY (refeicao_id, restricao_id)
);
CREATE TABLE IF NOT EXISTS cardapios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data_inicial TEXT NOT NULL,
    data_final TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS vincula_cardapio_refeicao (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cardapio_id INTEGER NOT NULL,
    refeicao_id INTEGER NOT NULL,
    data TEXT NOT NULL,
    tipo TEXT NOT NULL,
    FOREIGN KEY (cardapio_id)
        REFERENCES cardapios (id)
        ON DELETE CASCADE,
    FOREIGN KEY (refeicao_id)
        REFERENCES refeicoes (id)
        ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS aluno_falta (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    aluno_matricula TEXT NOT NULL,
    cardapio_id INTEGER NOT NULL,
    data TEXT NOT NULL,
    tipo TEXT NOT NULL,
    FOREIGN KEY (aluno_matricula)
        REFERENCES alunos (matricula)
        ON DELETE CASCADE,
    FOREIGN KEY (cardapio_id)
        REFERENCES cardapios (id)
        ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS justificativas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    aluno_falta_id INTEGER NOT NULL UNIQUE,
    motivo TEXT NOT NULL,
    FOREIGN KEY (aluno_falta_id)
        REFERENCES aluno_falta (id)
        ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS analise_justificativa (
    justificativa_id INTEGER PRIMARY KEY,
    aprovacao INTEGER NOT NULL,
    FOREIGN KEY (justificativa_id)
        REFERENCES justificativas (id)
        ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS avaliacoes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nota INTEGER NOT NULL,
    aluno_matricula TEXT NOT NULL,
    refeicao_id INTEGER NOT NULL,
    conteudo TEXT,
    titulo TEXT,
    FOREIGN KEY (aluno_matricula)
        REFERENCES alunos (matricula)
        ON DELETE CASCADE,
    FOREIGN KEY (refeicao_id)
        REFERENCES refeicoes (id)
        ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS notificacoes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    conteudo TEXT
);
CREATE TABLE IF NOT EXISTS notificacao_aluno (
    notificacao_id INTEGER NOT NULL,
    aluno_matricula TEXT NOT NULL,
    FOREIGN KEY (notificacao_id)
        REFERENCES notificacoes (id)
        ON DELETE CASCADE,
    FOREIGN KEY (aluno_matricula)
        REFERENCES alunos (matricula)
        ON DELETE CASCADE,
    PRIMARY KEY (notificacao_id, aluno_matricula)
);
