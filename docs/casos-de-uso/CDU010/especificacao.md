# CDU010 – Gerenciar Notificação

**Ator Primário:** Coordenador.  
**Descrição:** Este caso de uso permite que o Coordenador gerencie as notificações do sistema, possibilitando o cadastro, a edição e a exclusão de notificações destinadas aos alunos.
**Pré-condições:** Usuário deve estar logado como Coordenador.  
**Pós-condições:** Notificações podem ser modificadas.  

## Fluxo Principal

1. O coordenador acessa o sistema com login de coordenador.
2. O coordenador seleciona a opção "Gerenciar Notificações".
3. O sistema exibe um painel com as notificações e as opções para enviar, editar ou excluir notificações.
4. O sistema valida e salva as alterações realizadas.


## Fluxo de Exceção
- **FE1 – Dados inválidos:**  
    Caso, no momento da validação, as informações informadas estejam inválidas ou incompletas, o sistema exibe uma mensagem de erro e solicita ao Coordenador a correção dos dados, retornando ao passo 3 do Fluxo Principal.
