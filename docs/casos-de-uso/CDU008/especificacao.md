# CDU008 – Gerenciar Alunos

**Ator Primário:** Coordenador.  
**Descrição:** Permite que a coordenação gerencie os alunos cadastrados no sistema.  
**Pré-condições:** Usuário deve estar logado como Coordenador.    
**Pós-condições:** Dados sobre os alunos podem ser modificados.  

## Fluxo Principal

1. O coordenador seleciona a opção "Gerenciar Alunos".
2. O sistema apresenta a tela “Gerenciar Alunos” com abas funcionais (Visualizar, Adicionar, Atualizar e Deletar).
3. O sistema abre por padrão a aba "Visualizar", exibindo os alunos cadastrados.

## Fluxos Alternativos
**FA1 – Adicionar Aluno**

Ponto de inserção: Após o passo 2 do Fluxo Principal, quando o coordenador seleciona a aba "Adicionar".

1. O sistema exibe os campos "Matrícula do Aluno", "Nome do Aluno", "Senha do Aluno" e um campo de seleção para Restrições Alimentares.
2. O coordenador informa a matrícula, o nome e a senha do aluno.
3. O coordenador seleciona, se desejar, as restrições alimentares do aluno.
4. O coordenador clica no botão "Adicionar".
5. O sistema valida os dados informados.
6. O sistema cadastra o novo aluno.

**FA2 – Atualizar Aluno**

**Ponto de inserção:** Após o passo 2 do Fluxo Principal, quando o coordenador seleciona a aba "Atualizar".

1. O sistema exibe um campo de seleção com os alunos cadastrados.
2. O coordenador seleciona um aluno.
3. O sistema exibe os campos de matrícula (não editável), nome, senha e restrições alimentares.
4. O coordenador altera as informações desejadas.
5. O coordenador clica no botão "Atualizar".
6. O sistema valida e salva as alterações.

**FA3 – Deletar Aluno**

**Ponto de inserção:** Após o passo 2 do Fluxo Principal, quando o coordenador seleciona a aba "Deletar".

1. O sistema exibe um campo de seleção com os alunos cadastrados.
2. O coordenador seleciona um aluno.
3. O coordenador clica no botão "Deletar".
4. O sistema remove o aluno do sistema.

## Fluxos de Exceção
**FE1 – Dados obrigatórios não preenchidos**

Pode ocorrer nos fluxos FA1 e FA2.

Caso o coordenador tente confirmar a operação sem preencher os campos obrigatórios, o sistema exibirá uma mensagem de erro e não concluirá a operação.
