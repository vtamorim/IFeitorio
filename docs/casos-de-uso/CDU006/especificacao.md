# CDU006 – Gerenciar Justificativa

**Ator Primário:** Coordenador.  
**Descrição:** Permite que a coordenação gerencie as justificativas de falta do almoço.  
**Pré-condições:** O usuário deve estar logado como coordenador.  
**Pós-condições:** A justificativa selecionada terá seu status atualizado para aprovada ou recusada.  

## Fluxo Principal

1. O coordenador seleciona a opção "Gerenciar Justificativas de Faltas".
2. O sistema apresenta a tela “Gerenciar Justificativas de Faltas” com abas funcionais (Ver não analisadas, Ver analisadas e Analisar).
3. O sistema abre por padrão a aba "Ver não analisadas", exibindo as justificativas pendentes.

## Fluxos Alternativos

**FA1 – Visualizar Justificativas Analisadas**

**Ponto de inserção:** Após o passo 2 do Fluxo Principal, quando o coordenador seleciona a aba "Ver analisadas".

O sistema exibe a lista de justificativas já analisadas, com seus respectivos status.

**FA2 – Analisar Justificativa**

**Ponto de inserção:** Após o passo 2 do Fluxo Principal, quando o coordenador seleciona a aba "Analisar".

1. O sistema exibe um campo de seleção contendo as justificativas disponíveis.
2. O coordenador seleciona uma justificativa.
3. O sistema exibe as informações da justificativa selecionada, incluindo: aluno, cardápio, data, tipo de refeição e motivo da falta.
4. O coordenador avalia a justificativa.
5. O coordenador marca ou não a opção "Aprovar Justificativa".
6. O coordenador clica no botão "Analisar".
7. O sistema registra a decisão da coordenação.
8. O sistema atualiza o status da justificativa e notifica o aluno sobre o resultado.