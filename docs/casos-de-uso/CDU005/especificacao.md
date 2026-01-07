# CDU005 – Justificar Falta no Almoço
        
**Ator Primário:** Aluno.  
**Descrição:** Permite que o aluno envie uma justificativa de falta no almoço para o coordenador.
**Pré-condições:** O usuario deve estar logado como aluno, possuir o auxilio do almoço e ter faltado.  
**Pós-condições:** O coordenador recebe a justificativa enviada pelo aluno.

## Fluxo Principal

1. O aluno acessa a página de justificativa de falta no almoço.
2. O sistema exibe os campos "Selecionar Falta" e "Motivo da Falta".
3. O aluno seleciona o dia em que houve a falta.
4. O aluno preenche o motivo da falta.
5. O aluno clica no botão "Enviar".
6. O sistema valida os dados informados, registra a justificativa e a envia para o coordenador.


## Fluxos De Exceção

- **FE1 - Dados obrigatórios não preenchidos**
Caso o aluno tente enviar a justificativa com algum campo obrigatório não preenchido, o sistema exibirá a mensagem de erro:
"Campos vazios, tente novamente", e a operação não será concluída.
