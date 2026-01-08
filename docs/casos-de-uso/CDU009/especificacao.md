# CDU009 – Gerenciar Restrições

**Ator Primário:** Coordenador.  
**Descrição:** Permite que o coordenador gerencie as restrições alimentares cadastradas no sistema (ex.: vegetariano, intolerância à lactose, etc.)..  
**Pré-condições:** Usuário deve estar logado como Coordenador.  
**Pós-condições:** Dados sobre as restrições podem ser modificados.  

## Fluxo Principal

1. O coordenador seleciona a opção "Gerenciar Restrições Alimentares".
2. O sistema apresenta a tela “Gerenciar Restrições Alimentares” com abas funcionais (Visualizar, Adicionar, Atualizar e Deletar).
3. O sistema abre por padrão a aba "Visualizar", permitindo consultar as restrições cadastradas.

## Fluxos Alternativos
**FA1 – Adicionar Restrição Alimentar**

**Ponto de inserção:** Após o passo 2 do Fluxo Principal, quando o coordenador seleciona a aba "Adicionar".

1. O sistema exibe o campo "Nome da Restrição".
2. O coordenador informa o nome da restrição alimentar.
3. O coordenador clica no botão "Adicionar".
4. O sistema valida os dados informados.
5. O sistema salva a nova restrição alimentar.

**FA2 – Atualizar Restrição Alimentar**

**Ponto de inserção:** Após o passo 2 do Fluxo Principal, quando o coordenador seleciona a aba "Atualizar".

1. O sistema exibe um campo de seleção com as restrições alimentares cadastradas.
2. O coordenador seleciona uma restrição.
3. O sistema exibe o campo para edição do nome da restrição.
4. O coordenador altera a informação desejada.
5. O coordenador clica no botão "Atualizar".
6. O sistema valida e salva as alterações.

**FA3 – Deletar Restrição Alimentar**

**Ponto de inserção:** Após o passo 2 do Fluxo Principal, quando o coordenador seleciona a aba "Deletar".

1. O sistema exibe um campo de seleção com as restrições alimentares cadastradas.
2. O coordenador seleciona uma restrição.
3. O coordenador clica no botão "Deletar".
4. O sistema remove a restrição do sistema.

## Fluxos de Exceção
**FE1 – Dados inválidos ou campo vazio**

Pode ocorrer nos fluxos FA1 e FA2.

Caso o coordenador tente confirmar a operação com o campo obrigatório não preenchido, o sistema exibirá uma mensagem de erro e não concluirá a operação.

