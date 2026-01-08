# CDU010 – Gerenciar Notificação

**Ator Primário:** Coordenador.  
**Descrição:** Este caso de uso permite que o Coordenador gerencie as notificações do sistema, possibilitando o cadastro, a edição e a exclusão de notificações destinadas aos alunos.
**Pré-condições:** Usuário deve estar logado como Coordenador.  
**Pós-condições:** Notificações podem ser modificadas.  

## Fluxo Principal

1. O coordenador seleciona a opção "Gerenciar Notificações".
2. O sistema apresenta a tela “Gerenciar Notificações” com abas funcionais (Visualizar, Enviar, Atualizar e Deletar).
3. O sistema abre por padrão a aba "Visualizar", exibindo as notificações cadastradas.

## Fluxos Alternativos

**FA1 – Enviar Notificação**
**Ponto de inserção:** Após o passo 2 do Fluxo Principal, quando o coordenador seleciona a aba "Enviar".
1. O sistema exibe os campos "Título" e "Conteúdo" da notificação.
2. O sistema exibe a opção "Selecionar todos os alunos" e um campo de seleção de alunos destinatários.
3. O coordenador informa o título e o conteúdo da notificação.
4. O coordenador seleciona os alunos destinatários ou marca a opção de envio para todos.
5. O coordenador clica no botão "Enviar".
6. O sistema valida os dados informados.
7. O sistema envia a notificação aos alunos selecionados.

**FA2 – Atualizar Notificação**

**Ponto de inserção:** Após o passo 2 do Fluxo Principal, quando o coordenador seleciona a aba "Atualizar".

1. O sistema exibe um campo de seleção com as notificações cadastradas.
2. O coordenador seleciona uma notificação.
3. O sistema exibe os campos de título e conteúdo para edição.
4. O coordenador altera as informações desejadas.
5. O coordenador clica no botão "Atualizar".
6. O sistema valida e salva as alterações.

**FA3 – Deletar Notificação**

**Ponto de inserção:** Após o passo 2 do Fluxo Principal, quando o coordenador seleciona a aba "Deletar".

1. O sistema exibe um campo de seleção com as notificações cadastradas.
2. O coordenador seleciona uma notificação.
3. O coordenador clica no botão "Deletar".
4. O sistema remove a notificação do sistema.

## Fluxos de Exceção
**FE1 – Dados obrigatórios não preenchidos**

Pode ocorrer nos fluxos FA1 e FA2.

Caso o coordenador tente confirmar a operação sem preencher os campos obrigatórios, o sistema exibirá uma mensagem de erro e não concluirá a operação.