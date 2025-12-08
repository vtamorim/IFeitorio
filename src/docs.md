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
- id [PK]
- matricula
- nome
- senha
- restricoes ( lista de restrições que o aluno tem )

restricoes_alimentares
- id [PK] 
- nome

aluno_restricao
- aluno_id [PK]
- restricao_id [PK]

coordenadores
- id [PK]
- matricula
- nome
- senha

refeicao
- id [PK]
- nome
- descricao (explicar esse atributo melhor)

refeicao_restricao_alimentar
- refeicao_id [PK]
- restricao_id [PK]

cardapio
- data_inicial [PK] (talvez tirar o PK da data_inicial e colocar um id como PK)
- data_final

vincula_cardapio_refeicao
- cardapio_data_inicial [PK] (identificador do cardápio)
- refeicao_id [PK]
- data (dia da refeicao naquele cardapio)
- tipo (lanche, almoço, jantar)

aluno_falta
- id [PK]
- aluno_id
- cardapio_id
- refeicao_id

justificativa
- id [PK]
- aluno_falta_id
- motivo

analise_justificativa
- id [PK]
- aprovacao (talvez um bool se foi aceita a justificativa do aluno?)
- justificativa_id
- coordenador_id

avaliacao
- id [PK]
- nota
- aluno_id
- refeicao_id

- conteudo
- titulo 

notificacao
- id [PK]
- titulo
- conteudo

notificacao_aluno
- notificacao_id [PK]
- aluno_id [PK]
