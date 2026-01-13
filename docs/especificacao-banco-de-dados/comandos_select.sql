-- a) Lista todos os alunos.
SELECT * FROM alunos;

-- b) Lista o nome e a senha do aluno de matrícula '20241011110001'.
SELECT nome, senha
FROM alunos
WHERE matricula = '20241011110001';

-- c) Lista o nome e a senha dos alunos de matrícula '20241011110001' e '20241011110002'.
SELECT nome, senha
FROM alunos
WHERE matricula = '20241011110001' OR matricula = '20241011110002';

-- d) Lista a nota média das avaliações de cada refeição que o usuário deixou um conteúdo escrito na avaliação.
SELECT refeicao_id, AVG(nota)
FROM avaliacoes
WHERE conteudo IS NOT NULL
GROUP BY refeicao_id;

-- e) Lista as avaliações com nota acima da média de nota de todas as avaliações.
SELECT *
FROM avaliacoes
WHERE nota > (
    SELECT AVG(nota)
    FROM avaliacoes
);
