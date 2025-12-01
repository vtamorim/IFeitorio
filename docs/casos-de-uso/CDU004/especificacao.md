# CDU004 – Abrir Conta

**Ator Primário:** Visitante.  
**Descrição:** Permite o visitante abrir a sua conta.  
**Pré-condições:** *Nenhuma*.
**Pós-condições:** O usuário deve ter a sua conta cadastrada no sistema.
## Fluxo Principal

1. O aluno acessa o aplicativo e coloque os dados necessários( matrícula e senha).
2. O aluno seleciona o botão "Abrir Conta".
3. O sistema salva as informações dos dados registrados.

## Fluxo de Exceção

- **FE3 – Conta já registrada**

    **Ponto de inserção:** Após o passo 2 do Fluxo Principal
Caso os dados registrados pelo usuário já estejam inseridos no sistema, o próprio sistema exibirá uma mensagem de erro "Esta conta já está cadastrada, Tente Novamente"
