# CDU001 – Iniciar Sessão

**Ator Primário:** Visistante.  
**Descrição:** Permite que o usuário faça login no sistema utilizando sua matrícula e senha.  
**Pré-condições:** *Nenhuma*.  
**Pós-condições:** Usuário estará logado.  

## Fluxo Principal

1. O usuário abre o aplicativo.
2. O sistema exibe a tela de login.
3. O usuário informa sua matrícula e senha.
4. O sistema valida as credenciais.
5. O sistema identifica se o usuário é aluno ou coordenador.
6. O sistema exibe o menu de funcionalidades correspondente ao perfil do usuário.

## Fluxos De Exceção

- **FE1 – Dados inválidos:**  
  Se o usuário digitar matrícula ou senha incorretos, o sistema exibirá uma mensagem de erro e solicitará nova tentativa.
