# CDU009 – Gerenciar Restrições

**Ator Primário:** Coordenador.  
**Descrição:** Permite que o coordenador gerencie as restrições alimentares cadastradas no sistema (ex.: vegetariano, intolerância à lactose, etc.)..  
**Pré-condições:** O usuário deve estar autenticado no sistema como Coordenador.  
**Pós-condições:** Dados sobre as restrições podem ser modificados.  

## Fluxo Principal

1. O coordenador acessa o sistema com login de coordenador.
2. O coordenador seleciona a opção "Gerenciar Restrições".
3. O sistema exibe a lista de restrições cadastradas.
4. O coordenador pode editá-las, adicionar ou excluir uma restrição.
5. O sistema valida e salva as alterações realizadas.

## Fluxo de Exceção
- **FE1 – Dados inválidos:**  
    Caso, no momento da validação, as informações informadas estejam inválidas ou incompletas, o sistema exibe uma mensagem de erro e solicita ao Coordenador a correção dos dados, retornando ao passo 4 do Fluxo Principal.
