# CDU012 – Cadastrar Comunicados

**Ator Primário:** Coordenador.  
**Descrição:** Permite o coordenador cadastrar e enviar um comunicado/notificação aos alunos.  
**Pré-condições:** Usuário deve está logado como Coordenador.  
**Pós-condições:** Um Comunicado será Cadastrado.  

## Fluxo Principal

1. O coordenador acessa o sistema com login de coordenador.
2. O coordenador seleciona a opção "Gerenciar Notificações".
3. O sistema exibe um painel com as notificações e as opções para enviar, editar ou excluir notificações.
4. O coordenador seleciona a opção para enviar notificações.
5. O sistema exibe um formulário para o cadastro do comunicado.
6. O coordenador preenche os dados e seleciona a opção de "Cadastrar".
7. O sistema cadastra, salva e envia o comunicado ao(s) aluno(s).

## Fluxos De Exceção

- **FE1 – Dados incompletos/incorretos:**  
6. Caso o coordenador tente cadastrar um comunicado com campos obrigatórios em branco ou com dados incorretos, o sistema exibirá um aviso e não salvará as alterações.
