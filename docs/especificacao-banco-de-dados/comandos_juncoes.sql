-- a) 1 - Todos os Alunos com alguma restrição.
SELECT a.matricula, ar.restricao_id
FROM alunos a
INNER JOIN aluno_restricao ar ON a.matricula = ar.aluno_matricula;

-- a) 2 - Todas as refeições com alguma restrição.
SELECT r.id AS refeicao_id, rr.restricao_id
FROM refeicoes r
INNER JOIN refeicao_restricao_alimentar rr ON r.id = rr.refeicao_id;

-- a) 3 - Todas as faltas com justificativa.
SELECT af.id, af.aluno_matricula, af.cardapio_id, af.data, af.tipo, j.motivo
FROM aluno_falta af
INNER JOIN justificativas j ON af.id = j.aluno_falta_id;

-- b) 1 - Todos os alunos, incluindo suas restrições alimentares.
SELECT
    a.matricula, a.nome, a.senha,
    r.id AS ra_id, r.nome AS ra_nome
FROM
    alunos a
LEFT JOIN aluno_restricao ar ON a.matricula = ar.aluno_matricula
LEFT JOIN restricoes_alimentares r ON ar.restricao_id = r.id
ORDER BY a.matricula;

-- b) 2 - Todas as refeições, incluindo suas restrições alimentares compatíveis.
SELECT 
    r.id, r.nome, r.descricao,
    ra.id AS ra_id, ra.nome AS ra_nome
FROM
    restricoes_alimentares ra
RIGHT JOIN refeicao_restricao_alimentar rra ON rra.restricao_id = ra.id
RIGHT JOIN refeicoes r ON r.id = rra.refeicao_id
ORDER BY r.id;

-- c) Todas as refeições e restrições.
SELECT 
    r.id AS refeicao_id, r.nome AS refeicao_nome, r.descricao AS refeicao_descricao,
    ra.id AS restricao_id, ra.nome AS restricao_nome
FROM refeicoes r
FULL OUTER JOIN refeicao_restricao_alimentar rra ON r.id = rra.refeicao_id
FULL OUTER JOIN restricoes_alimentares ra ON ra.id = rra.restricao_id
ORDER BY r.id;
