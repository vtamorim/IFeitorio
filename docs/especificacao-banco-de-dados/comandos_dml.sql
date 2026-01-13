-- a) Atualiza todos as senhas dos alunos para '666'.
UPDATE alunos 
SET senha = '666';

-- b) Atualiza a senha do aluno de matrícula '20241011110001'.
UPDATE alunos 
SET senha = '111' 
WHERE matricula = '20241011110001';

-- c) Muda o tipo da(s) refeição(ões) de id 2 cadastrada(s) no cardápio de id 2.
UPDATE vincula_cardapio_refeicao 
SET tipo = 'lanche_tarde' 
WHERE cardapio_id = 2 AND refeicao_id = 2;

-- d) Altera o nome e a senha do coordenador de matrícula '111',
UPDATE coordenadores
SET nome = 'Gilbert da Silva',
    senha = '1111'
WHERE matricula = '111';

-- e) Duplica a senha do coordenador nela mesma.
UPDATE coordenadores
SET senha = senha || senha
WHERE matricula = '111';

-- f) Todos os nomes dos alunos ficam em maiúsculas.
UPDATE alunos
SET nome = UPPER(nome);

-- g) Deleta todos os alunos.
DELETE FROM alunos;

-- h) Deleta o aluno de matrícula '20241011110001'.
DELETE FROM alunos
WHERE matricula = '20241011110001';

-- i) Deleta os alunos de matrícula '20241011110002' e '20241011110003'.
DELETE FROM alunos
WHERE matricula = '20241011110002' OR matricula = '20241011110003';

-- j) Deleta a falta com o menor 'id'.
DELETE FROM aluno_falta
WHERE id = (
    SELECT MIN(id) FROM aluno_falta
);
