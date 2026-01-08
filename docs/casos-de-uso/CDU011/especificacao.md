# CDU011 – Gerenciar faltas dos alunos

**Ator Primário:** Coordenador.  
**Descrição:** Permite o coordenador adicionar ou editar as faltas dos alunos.  
**Pré-condições:** O usuário deve estar logado como coordenador.  
**Pós-condições:** Algumas faltas podem ser adicionadas ou excluídas.  

## Fluxo Principal

1. O coordenador seleciona a opção "Gerenciar Faltas".
2. O sistema apresenta a tela “Gerenciar Faltas” com abas funcionais (Visualizar, Adicionar e Deletar).
3. O sistema abre por padrão a aba "Visualizar", exibindo as faltas registradas.

## Fluxos Alternativos
**FA1 – Adicionar Falta**

**Ponto de inserção:** Após o passo 2 do Fluxo Principal, quando o coordenador seleciona a aba "Adicionar".

1. O sistema exibe um campo de seleção para o cardápio.
2. O coordenador seleciona um cardápio.
3. O sistema exibe um campo de seleção para a data correspondente ao cardápio selecionado, um campo de seleção para o tipo de refeição, um campo de seleção para o aluno.
4. O coordenador seleciona a data, tipo de refeição e o aluno.
5. O coordenador clica no botão "Adicionar".
6. O sistema valida os dados informados.
7. O sistema registra a falta do aluno.

**FA2 – Deletar Falta**

**Ponto de inserção:** Após o passo 2 do Fluxo Principal, quando o coordenador seleciona a aba "Deletar".

1. O sistema exibe um campo de seleção com as faltas registradas.
2. O coordenador seleciona uma falta.
3. O coordenador clica no botão "Deletar".
4. O sistema remove a falta do sistema.

**Fluxos de Exceção**
**FE1 – Dados obrigatórios não preenchidos**

Pode ocorrer no fluxo FA1 – Adicionar Falta.

Caso o coordenador tente registrar a falta sem preencher todos os campos obrigatórios, o sistema exibirá uma mensagem de erro e não concluirá a operação.