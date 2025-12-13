Resumo do resumo sobre o que o programa irá fazer

O programa deve facilitar o sistema de ver os cardápios semanais do IFRN.
O visitante se cadastrará com matrícula e senha.

Os alunos poderão:
- cadastrar suas restrições alimentares em suas contas
- receberem notificações sobre alterações nos cardápios ou outras coisas
- avaliar refeições dos cardápios
- justificar faltas em refeições de algum cardápio em algum dia específico

os coordenadores poderão:
- modificar as restrições alimentares disponíveis
- modificar as refeições e cardápios disponíveis
- modificar as avaliações realizadas
- enviar notificações para os alunos
- definir se algum aluno faltou uma refeição
- analisar as justificativas de faltas

Os cardápios serão de um dia até algum outro dia (semanal, provavelmente).
Eles terão diversas refeições integradas.
Os alunos avaliam uma refeição específica.
Algumas refeições dos cardápios esterão classificadas para alguma restrição alimentar em específico.




---
Tabelas do Banco de Dados (nova)


alunos
- matricula [PK]
- nome
- senha

restricoes_alimentares
- id [PK] 
- nome

aluno_restricao
- aluno_matricula [PK] [FK]
- restricao_id [PK] [FK]

coordenadores
- matricula [PK]
- nome
- senha

refeicoes
- id [PK]
- nome
- descricao [O]

refeicao_restricao_alimentar
- refeicao_id [PK] [FK]
- restricao_id [PK] [FK]

cardapios
- id [PK]
- data_inicial
- data_final

vincula_cardapio_refeicao
- id [PK] (Acho q devemos pôr um id, pois o cardápio e o refeicao_id como PK faria com que não fosse possível repetir um prato em uma mesma semana... Provavelmente todos esses 4 valores abaixo devem ser únicos entre si, ou 3 tirando o refeicao_id)
- cardapio_id [FK] (identificador do cardápio)
- refeicao_id [FK]
- data (dia da refeicao naquele cardapio)
- tipo (lanche manhã/tarde/noite, almoço, jantar)

aluno_falta
- id [PK]
- aluno_matricula [FK]
- cardapio_id [FK]
- data
- tipo (almoço, jantar)

justificativas
- id [PK]
- aluno_falta_id [FK]
- motivo

analise_justificativa
- id [PK]
- aprovacao (talvez um bool se foi aceita a justificativa do aluno?)
- justificativa_id [FK]
- coordenador_matricula [FK]

avaliacoes
- id [PK]
- nota
- aluno_matricula [FK]
- refeicao_id [FK]
- conteudo [O]
- titulo [O]

notificacoes
- id [PK]
- titulo
- conteudo [O]

notificacao_aluno
- notificacao_id [PK] [FK]
- aluno_matricula [PK] [FK]


---
Código SQLite


PRAGMA foreign_keys = ON;
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
    aluno_falta_id INTEGER NOT NULL,
    motivo TEXT NOT NULL,
    FOREIGN KEY (aluno_falta_id)
        REFERENCES aluno_falta (id)
        ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS analise_justificativa (
    justificativa_id INTEGER PRIMARY KEY,
    aprovacao INTEGER NOT NULL,
    coordenador_matricula TEXT NOT NULL,
    FOREIGN KEY (justificativa_id)
        REFERENCES justificativas (id)
        ON DELETE CASCADE,
    FOREIGN KEY (coordenador_matricula)
        REFERENCES coordenadores (matricula)
        ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS avaliacoes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nota REAL NOT NULL,
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

---
models

Aluno
- matricula: str
- nome: str
- senha: str
- restricoes: list[Restricao]

Restricao
- id: int
- nome: str

Coordenador
- matricula: str
- nome: str
- senha: str

Refeicao
- id: int
- nome: str
- descricao: Optional[str]
- restricoes_compatives: list[Restricao]
- data: Optional[date]
- tipo: Optional[str]

Cardapio
- id: int
- data_inicial: date
- data_final: date
- refeicoes: list[Refeicao]

Falta
- id: int
- aluno: Aluno
- cardapio: Cardapio
- data: date
- tipo: str

Justificativa
- id: int
- falta: Falta
- motivo: str
- aprovada: Optional[bool]
- coordenador: Optional[Coordenador]

Avaliacao
- id: int
- nota: float
- aluno: Aluno
- refeicao: Refeicao
- conteudo: Optional[str]
- titulo: Optional[str]

Notificacao
- id: int
- titulo: str
- conteudo: Optional[str]
- alunos: list[Aluno]
