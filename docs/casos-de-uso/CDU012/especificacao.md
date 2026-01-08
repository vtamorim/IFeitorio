# CDU012 – Cadastrar Comunicados

**Ator Primário:** Coordenador.  
**Descrição:** Este caso de uso permite que o Coordenador cadastre e envie comunicados aos alunos por meio do sistema.  
**Pré-condições:** Usuário deve estar logado como Coordenador.  
**Pós-condições:** Um Comunicado será Cadastrado no Sistema e disponibilizados para os alunos.  

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
Caso, no passo 6 do Fluxo Principal, existam campos obrigatórios não preenchidos ou dados inválidos, o sistema exibe uma mensagem de erro e solicita a correção das informações, retornando ao formulário de cadastro.