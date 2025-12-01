# CDU003 – Cadastrar Restrição Alimentar

**Ator Primário:** Aluno.  
**Descrição:** Permite o aluno registrar suas restrições alimentares.  
**Pré-condições:** O usuário deve estar cadastrado como aluno.  
**Pós-condições:** O aluno cadastrará suas restrições alimentares no sistema.  

## Fluxo Principal

1. O aluno acessa o aplicativo e faz login.
2. O aluno seleciona a opção "Minhas Restrições".
3. O aluno preenche os campos informando suas restrições (ex: vegetariano, intolerância à lactose).
4. O sistema salva as informações e as vincula à matrícula do aluno.

## Fluxo Alternativo 

- **FA3 – Remover restrição existente**

    **Ponto de inserção:** Após o passo 2 do Fluxo Principal
O aluno pode optar por excluir uma ou mais restrições previamente cadastradas. O sistema exibirá uma lista das restrições atuais e permitirá que o aluno selecione quais deseja remover. Antes da exclusão, o sistema solicitará uma confirmação para evitar remoções acidentais.

**Fluxo:**
1. O sistema exibe as restrições alimentares cadastradas para o aluno.
2. O aluno seleciona as restrições que deseja remover.
3. O sistema exibe uma mensagem de confirmação: "Tem certeza que deseja remover estas restrições?"
4. Se o aluno confirmar, o sistema remove as restrições selecionadas e exibe uma mensagem de sucesso.
5. Se o aluno cancelar, o sistema retorna à tela do perfil do usuário.
