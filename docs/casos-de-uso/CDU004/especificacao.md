# CDU004 – Abrir Conta

**Ator Primário:** Visitante.  
**Descrição:** Permite o visitante abrir a sua conta.  
**Pré-condições:** *Nenhuma*.  
**Pós-condições:** O usuário deve ter a sua conta cadastrada no sistema.

## Fluxo Principal

1. O sistema exibe os campos de matricula, nome, senha e restrição alimentar.
2. O visitante preenche os campos necessarios
3. o visitante clica no botão "abrir"
4. O sistema salva as informações dos dados registrados.

## Fluxo de Exceção

- **FE1 – Dados obrigatórios não preenchidos:** 
Caso o usuário tente abrir uma conta com algum campo obrigatório não preenchido, o sistema exibirá a mensagem de erro:
"Campos obrigatórios vazios, tente novamente", e a operação não será concluída.
- **FE2 – Conta já registrada**
Caso os dados registrados pelo usuário já estejam inseridos no sistema, o próprio sistema exibirá uma mensagem de erro "Matrícula já está sendo Utilizada", e a operação não será concluída.
