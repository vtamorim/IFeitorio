# Principais Casos de Uso

## CDU001 – Iniciar Sessão

**Ator Primário:** Aluno ou Coordenação/Administração  
**Descrição:** Permite que o usuário faça login no sistema utilizando sua matrícula e senha.

### Fluxo Principal

1. O usuário abre o aplicativo.
2. O sistema exibe a tela de login.
3. O usuário informa sua matrícula e senha.
4. O sistema valida as credenciais.
5. O sistema identifica se o usuário é aluno ou administrador.
6. O sistema exibe o menu de funcionalidades correspondente ao perfil do usuário.

### Fluxos De Exceção

- **FE1 – Dados inválidos:**  
  Se o usuário digitar matrícula ou senha incorretos, o sistema exibirá uma mensagem de erro e solicitará nova tentativa.

## CDU002 – Gerenciar Cardápio

**Ator Primário:** Coordenação/Administração  
**Descrição:** Permite que a coordenação cadastre ou edite o cardápio semanal.

### Fluxo Principal

1. O administrador acessa o sistema com login de administrador.
2. O administrador seleciona a opção "Gerenciar Cardápio".
3. O sistema exibe as opções: "Cadastrar novo cardápio" ou "Editar cardápio existente".
4. O administrador insere ou altera as informações de cada refeição (ex: data, turno, pratos).
5. O administrador salva as alterações.
6. O sistema atualiza o cardápio e envia notificações aos alunos.

### Fluxos De Exceção

- **FE1 – Dados incompletos:**  
  Caso o administrador tente salvar um cardápio com campos obrigatórios em branco, o sistema exibirá um aviso.

## CDU003 – Cadastrar Restrição Alimentar

**Ator Primário:** Aluno  
**Descrição:** Permite ao aluno registrar suas restrições alimentares.

### Fluxo Principal

1. O aluno acessa o aplicativo e faz login.
2. O aluno seleciona a opção "Minhas Restrições".
3. O aluno preenche os campos informando suas restrições (ex: vegetariano, intolerância à lactose).
4. O sistema salva as informações e as vincula à matrícula do aluno.

### Fluxo Alternativo 

- **FA3 – Remover restrição existente**

    **Ponto de inserção:** Após o passo 2 do Fluxo Principal
O aluno pode optar por excluir uma ou mais restrições previamente cadastradas. O sistema exibirá uma lista das restrições atuais e permitirá que o aluno selecione quais deseja remover. Antes da exclusão, o sistema solicitará uma confirmação para evitar remoções acidentais.

**Fluxo:**
1. O sistema exibe as restrições alimentares cadastradas para o aluno.
2. O aluno seleciona as restrições que deseja remover.
3. O sistema exibe uma mensagem de confirmação: "Tem certeza que deseja remover estas restrições?"
4. Se o aluno confirmar, o sistema remove as restrições selecionadas e exibe uma mensagem de sucesso.
5. Se o aluno cancelar, o sistema retorna à tela de
