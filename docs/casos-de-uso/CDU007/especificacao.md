# CDU007 – Gerenciar Avaliações

**Ator Primário:** Coordenador.  
**Descrição:** Permite que o coordenador visualize e delete avaliações realizadas pelos alunos sobre as refeições.  
**Pré-condições:** Usuário deve está logado como Coordenador.  
**Pós-condições:** As avaliações permanecem registradas ou são removidas do sistema.  

## Fluxo Principal

1. O coordenador seleciona a opção "Gerenciar Avaliações".
2. O sistema exibe a tela com as abas Visualizar e Deletar.
3. O sistema abre por padrão a aba "Visualizar".
4. O sistema exibe um campo de seleção para escolha da refeição.
5. O coordenador seleciona uma refeição.
6. O sistema exibe as avaliações relacionadas à refeição selecionada.
7. Para cada avaliação, o sistema apresenta:
    Identificação da avaliação
    Identificação do aluno
    Nota em formato de estrelas
    Título (quando informado)
    Comentário da avaliação

## Fluxos Alternativos

**FA1 – Deletar Avaliação**
- Ponto de inserção: Após o passo 2 do Fluxo Principal, caso o coordenador selecione a aba "Deletar".
1. O coordenador seleciona uma avaliação.
2. O coordenador clica no botão "deletar".
3. O sistema remove a avaliação selecionada.
4. O sistema atualiza a lista de avaliações exibidas.
