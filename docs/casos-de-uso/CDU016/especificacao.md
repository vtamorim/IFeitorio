# CDU016 – Gerenciar Refeições

**Ator Primário:** Coordenador.  
**Descrição:** Permite que o coordenador gerencie as refeições cadastradas no sistema.  
**Pré-condições:** Usuário deve estar logado como Coordenador.  
**Pós-condições:** Dados sobre as refeições podem ser modificados.  

## Fluxo Principal

1. O coordenador seleciona a opção "Gerenciar Refeições".
2. O sistema apresenta a tela “Gerenciar Refeições com abas funcionais (Visualizar, Adicionar, Atualizar e Deletar).
3. O sistema abre por padrão a aba "Visualizar", permitindo consultar as refeições cadastradas.

## Fluxos Alternativos

**FA1 – Adicionar Refeição**

**Ponto de inserção:** Após o passo 2 do Fluxo Principal, quando o coordenador seleciona a aba "Adicionar".

1. O sistema exibe os campos "Nome da Refeição", "Descrição da Refeição (Opcional)" e "Restrições Compatíveis com a Refeição".
2. O coordenador preenche os dados da refeição.
3. O coordenador clica no botão "Adicionar".
4. O sistema valida os dados informados.
5. O sistema salva a nova refeição.

**FA2 – Atualizar Refeição**

**Ponto de inserção:** Após o passo 2 do Fluxo Principal, quando o coordenador seleciona a aba "Atualizar".

1. O sistema exibe um campo de seleção com as refeições cadastradas.
2. O coordenador seleciona uma refeição.
3. O sistema exibe o campo para edição de todos os dados da refeição.
4. O coordenador altera os dados desejados.
5. O coordenador clica no botão "Atualizar".
6. O sistema valida e salva as alterações.

**FA3 – Deletar Refeição**

**Ponto de inserção:** Após o passo 2 do Fluxo Principal, quando o coordenador seleciona a aba "Deletar".

1. O sistema exibe um campo de seleção com as refeições cadastradas.
2. O coordenador seleciona uma refeição.
3. O coordenador clica no botão "Deletar".
4. O sistema remove a refeição do sistema.

## Fluxos de Exceção

**FE1 – Dados inválidos ou campo vazio**

Pode ocorrer nos fluxos FA1 e FA2.

Caso o coordenador tente confirmar a operação com algum campo obrigatório não preenchido, o sistema exibirá uma mensagem de erro e não concluirá a operação.
