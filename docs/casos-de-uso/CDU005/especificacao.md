# CDU005 – Justificar Falta no Almoço
        
**Ator Primário:** Aluno .  
**Descrição:** Permite o Aluno enviar a justificativa para o Coordenador.  
**Pré-condições:** O aluno deve possuir o auxilio do almoço, ter faltado.  
**Pós-condições:** O coordenador receber a justificativa do aluno que a enviou.  

## Fluxo Principal

1. O aluno acessa o sistema com o login de aluno.
2. O aluno entra na página de justificativa de forma direta.
3. O aluno insere os dados exigidos (data e o motivo).
4. O aluno seleciona o botão "Enviar justificativa".
5. O sistema registra a justificativa e a envia para o coordenador.

## Fluxo Alternativo 

- **FA1 - Ir para a Página de Justificativa pela notificação**
**Ponto de inserção:** Após o passo 1 do fluxo principal
2. O aluno entra na página de justificativa pela aba de notificações.
3. O aluno insere os dados exigidos (motivo).
4. O fluxo segue igual ao principal a partir do passo 3. 

## Fluxos De Exceção

- **FE1 - Inserir Dados Inválidos**

**Ponto de inserção:** Após o passo 4 de ambos os fluxos(principal e alternativo)
Se algum dos dados necessários não forem preenchidos, o sistema retornará um erro e pedirá que o aluno preencha os campos necessarios. 

5. O sistema retorna uma erro
6. O aluno é redirecionado para o passo 2 do fluxo principal