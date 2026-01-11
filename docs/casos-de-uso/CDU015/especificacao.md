# CDU015 – Analisar Refeição 

**Ator Primário:** Aluno.  
**Descrição:** Permitir o aluno avaliar e ver informações sobre uma refeição.  
**Pré-condições:** O usuario deve estar logado no sistema como aluno.  
**Pós-condições:** O sistema pode receber uma avaliação.

## Fluxo Principal

1. O usuário seleciona a opção "Analisar Refeição".
2. O sistema exibe um campo de seleção para escolha da refeição.
3. O usuário seleciona uma refeição.
4. O sistema exibe a nota média da refeição (se houver avaliações cadastradas no sistema), informações da refeição e a lista de avaliações realizadas por outros usuários, contendo nota, título e conteúdo.
5. O sistema exibe o formulário para avaliação da refeição.
6. O usuário informa a nota da refeição (obrigatória) em estrelas (1 a 5 estrelas).
7. O usuário pode informar opcionalmente o título e o conteúdo da avaliação.
8. O usuário clica no botão "Enviar".
9. O sistema registra a avaliação da refeição.

## Fluxos Alternativos

**FA1 – Atualizar Avaliação**
- Caso o usuário já tenha avaliado a refeição selecionada no passo 3, então o formulário exibirá um botão de "Atualizar", ao invés de "Enviar", e o sistema editará a avaliação caso o usuário prossiga com os passos 6 e 7.

## Fluxos de Exceção

**FE1 – Dados inválidos ou Campos Obrigatórios Vazios**
- Caso algum dado inválido ou campos obrigatórios estejam vazios sejam enviados pelo formulário, o sistema exibirá uma mensagem de erro e não efetuará a adição/edição da avaliação.
