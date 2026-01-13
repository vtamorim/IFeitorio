INSERT INTO alunos (matricula, nome, senha) 
VALUES 
    ('20241011110001', 'Ricardo Xavier de Lima', '111'),
    ('20241011110002', 'João Rafael Sobrinho Diogenes Florêncio', '222'),
    ('20241011110003', 'Victor Miguel Amorim do do Nascimento', '333'),
    ('20241011110004', 'Luna de Oliveira Bezerril Deodato', '444'),
    ('20241011110005', 'João Pedro Silva De Oliveira', '555');
INSERT INTO restricoes_alimentares (nome)
VALUES 
    ('Vegetariano'),
    ('Vegano'),
    ('Intolerância a Lactose'),
    ('Diabetes'),
    ('Sensibilidade ao Glúten');
INSERT INTO aluno_restricao (aluno_matricula, restricao_id) 
VALUES 
    ('20241011110001', 2),
    ('20241011110002', 3),
    ('20241011110002', 5),
    ('20241011110004', 5),
    ('20241011110005', 1);
INSERT INTO coordenadores (matricula, nome, senha) 
VALUES 
    ('111', 'Gilbert', '111'),
    ('222', 'Roberto', '222'),
    ('333', 'Demostenes', '333'),
    ('444', 'Júlia Gomes', '444'),
    ('555', 'Francisco', '555');
INSERT INTO refeicoes (nome, descricao) 
VALUES 
    ('Pão com Ovos', NULL),
    ('Sanduíche Natural', 'Pão com diversos ingredientes naturais dentro'),
    ('Suco de Manga', NULL),
    ('Macarronada', 'Macarrão com Frango'),
    ('Arroz com Frango', NULL);
INSERT INTO refeicao_restricao_alimentar (refeicao_id, restricao_id) 
VALUES 
    (2, 1),
    (2, 2),
    (2, 3),
    (2, 4),
    (3, 1);
INSERT INTO cardapios (data_inicial, data_final) 
VALUES 
    ('12/09/2026', '15/09/2026'),
    ('05/01/2026', '09/01/2026'),
    ('13/01/2026', '14/01/2026'),
    ('15/01/2026', '16/01/2026'),
    ('17/01/2026', '18/01/2026');
INSERT INTO vincula_cardapio_refeicao (cardapio_id, refeicao_id, data, tipo) 
VALUES 
    (2, 1, '05/01/2026', 'lanche_manha'),
    (2, 3, '05/01/2026', 'lanche_manha'),
    (2, 5, '05/01/2026', 'almoco'),
    (2, 3, '05/01/2026', 'almoco'),
    (2, 2, '05/01/2026', 'lanche_manha');
INSERT INTO aluno_falta (aluno_matricula, cardapio_id, data, tipo) 
VALUES 
    ('20241011110001', 2, '05/01/2026', 'almoco'),
    ('20241011110002', 2, '05/01/2026', 'almoco'),
    ('20241011110003', 2, '05/01/2026', 'almoco'),
    ('20241011110004', 2, '05/01/2026', 'almoco'),
    ('20241011110004', 2, '05/01/2026', 'jantar');
INSERT INTO justificativas (aluno_falta_id, motivo) 
VALUES 
    (1, 'Não sabia que isso existia'),
    (2, 'Não sei'),
    (3, 'Tava doente'),
    (4, 'Eu não faltei'),
    (5, 'Tava de férias');
INSERT INTO analise_justificativa (justificativa_id, aprovacao) 
VALUES 
    (1, 0),
    (2, 1),
    (3, 1),
    (4, 0),
    (5, 1);
INSERT INTO avaliacoes (nota, aluno_matricula, refeicao_id, conteudo, titulo) 
VALUES 
    (0, '20241011110001', 1, NULL, NULL),
    (1, '20241011110001', 1, NULL, NULL),
    (4, '20241011110002', 3, 'Bom', 'Suco muito bom'),
    (2, '20241011110002', 4, NULL, NULL),
    (4, '20241011110004', 5, NULL, 'Melhor prato');
INSERT INTO notificacoes (titulo, conteudo) 
VALUES 
    ('Falta Adicionada', NULL),
    ('Falta Adicionada', NULL),
    ('Falta Adicionada', NULL),
    ('Justificativa Analisada', 'Sua primeira justificativa foi analisada'),
    ('Cardápio Alterado', NULL);
INSERT INTO notificacao_aluno (notificacao_id, aluno_matricula) 
VALUES 
    (1, '20241011110001'),
    (2, '20241011110004'),
    (3, '20241011110004'),
    (4, '20241011110004'),
    (5, '20241011110005');
