# Visão de Produto

## Objetivo

<div style="font-size:2.9rem; color: red; position:absolute; top: 6.63rem; left: 8.5rem;" >.</div>
O sistema &nbsp;<b style="font-size:1.2rem; color: green">iFeitório</b>&nbsp; tem como objetivo gerenciar as ações relacionadas ao refeitório do Campus, como consultar o cardápio do dia/semana.

## Problema

Atualmente, os alunos do Instituto Federal do Rio Grande do Norte enfrentam dificuldades relacionadas ao acesso às informações da cantina escolar. O cardápio diário ou semanal raramente está disponível de forma prática e acessível, o que gera incerteza sobre as refeições oferecidas e pode resultar em:

* Filas desnecessárias
* Indecisão dos alunos
* Desperdício de alimentos

Além disso, o processo para justificar ausência em uma refeição é **burocrático**. Em muitos casos, os estudantes precisam abrir chamados, que podem ter resposta demorada por parte da coordenação. Essa falta de agilidade:

* Dificulta o controle da cantina sobre a frequência
* Prejudica a comunicação entre alunos e administração
* Impacta negativamente estudantes com motivos legítimos para não comparecer

## Solução do Problema

A solução proposta é o desenvolvimento de um **aplicativo** que permita:

* Consultar o cardápio do dia ou da semana
* Visualizar detalhes das refeições
* Justificar a falta no almoço de maneira prática
* Enviar sugestões e avaliar os pratos servidos

Esse sistema facilitaria o acesso à informação, melhoraria a organização da cantina e tornaria a comunicação entre alunos e coordenação mais eficiente.

## Perfis Envolvidos

Alunos: **todos os matriculados do Campus**.
- Precisam consultar o cardápio, justificar faltas e receber atualizações sobre o refeitório com mais facilidade.

Coordenadores: **todos os coordenadores matriculados do Campus**.
- Precisam definir e informar sobre alterações dos cardápios aos alunos.

Admin: **administra os alunos, coordenadores e o aplicativo**.


## Requisitos Funcionais

### Requisitos Gerais

#### RF001 – Login

O sistema deve permitir que os usuários façam login utilizando matrícula e senha. Após a autenticação, o sistema deve identificar se o usuário é aluno ou administrador, exibindo as funcionalidades correspondentes.

### Requisitos de Alunos

#### RF002 – Consultar Cardápio

O sistema deve permitir que os alunos visualizem o cardápio da semana (lanche e almoço).

#### RF003 – Cadastro de Restrição Alimentar

O sistema deve permitir que o aluno cadastre suas restrições alimentares, como vegetarianismo ou intolerância à lactose.

#### RF004 – Justificar Falta no Almoço

O aluno deve poder justificar sua ausência em uma refeição, informando o motivo da falta. Essa justificativa será enviada para análise da coordenação.

#### RF005 – Notificações de Atualização do Cardápio

O sistema deve enviar notificações aos alunos sempre que um novo cardápio for publicado ou alterado.

#### RF006 – Notificação de Avisos

O sistema deve enviar notificações aos alunos quando houver comunicados importantes da coordenação.

#### RF007 – Histórico de Justificativas de Falta

Os alunos devem poder consultar as justificativas já enviadas, o status de análise e as respostas da coordenação (ex.: "justificativa aceita" ou "recusada").

#### RF008 – Gerar QR-code

O sistema deve permitir que os alunos gerem um QR-code vinculado à sua matrícula para ser utilizado na identificação durante a retirada do lanche ou almoço.

#### RF009 – Avaliar as Refeições

Os alunos devem ter a opção de avaliar os pratos servidos, utilizando notas ou comentários, para fornecer feedback à equipe da cantina.

### Requisitos de Administradores

#### RF010 – Painel Administrativo para a Coordenação

O sistema deve oferecer uma área exclusiva para os administradores da cantina e da coordenação, onde poderão cadastrar e editar cardápios, visualizar justificativas recebidas, responder aos alunos e consultar estatísticas de uso.

#### RF011 – Enviar Cardápio

A coordenação deve conseguir cadastrar o cardápio semanal no sistema, informando as refeições que serão servidas.

#### RF012 – Atualizar Cardápio

O sistema deve permitir que a coordenação edite ou atualize o cardápio já cadastrado, caso haja mudanças de última hora.

#### RF013 – Envio de Comunicados pela Coordenação

A coordenação deve poder enviar avisos ou comunicados importantes para todos os alunos, como alterações no funcionamento da cantina ou eventos especiais.

#### RF014 – Verificação de Justificativa

A coordenação deve poder acessar as justificativas de falta ao almoço e avaliá-las como aceitas ou recusadas.

#### RF015 – Verificação de Dados

O sistema deve permitir que a coordenação visualize dados de frequência dos alunos no lanche e no almoço, incluindo dias mais frequentados, quantidades servidas e avaliações dos pratos, a fim de auxiliar no controle de desperdício e planejamento de refeições.

## Requisitos Não-Funcionais

- Deve ser feito em **Python** e **Streamlit**.
- O Banco de Dados deve ser o **SQLite**.
