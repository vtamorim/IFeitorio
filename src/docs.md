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
- tipo (lanche, almoço, jantar)

refeicao_restricao_alimentar
- refeicao_id [PK]
- restricao_id [PK]

cardapios
- id [PK]
- data_inicial
- data_final

vincula_cardapio_refeicao
- id [PK] (Acho q devemos pôr um id, pois o cardápio e o refeicao_id como PK faria com que não fosse possível repetir um prato em uma mesma semana... Provavelmente todos esses 4 valores abaixo devem ser únicos entre si, ou 3 tirando o refeicao_id)
- cardapio_id (identificador do cardápio)
- refeicao_id
- data (dia da refeicao naquele cardapio)

aluno_falta
- id [PK]
- aluno_id
- vincula_cardapio_refeicao_id

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
