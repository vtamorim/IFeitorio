# CDU002 – Gerenciar Cardápio

**Ator Primário:** Coordenação.  
**Descrição:** Permite que a coordenação gerencie o cardápio semanal.  
**Pré-condições:** Usuário deve está logado como Coordenador.  
**Pós-condições:** Os cardápios semanais serão modificados.  

## Fluxo Principal

1. O coordenador acessa o sistema com login de coordenador.
2. O coordenador seleciona a opção "Gerenciar Cardápio".
3. O sistema exibe as opções de "Cadastrar Cardápio", "Editar Cardápio", "Excluir Cardápio" e "Visualizar Cardápios".
4. O coordenador seleciona a sua opção e altera as informações de cada refeição (ex: data, turno, pratos).
5. O coordenador salva as alterações.
6. O sistema atualiza o cardápio e envia notificações aos alunos.

## Fluxos De Exceção

- **FE1 – Dados incompletos:**  
4. Caso o coordenador tente salvar um cardápio com campos obrigatórios em branco, o sistema exibirá um aviso e não salvará as alterações.
