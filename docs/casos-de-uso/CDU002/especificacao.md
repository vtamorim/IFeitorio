# CDU002 – Gerenciar Cardápio

**Ator Primário:** Coordenação.  
**Descrição:** Permite que a coordenação visualize, adicione, atualize e delete os cardápios semanais, definindo informações como data, turno e pratos.  
**Pré-condições:** Usuário deve estar logado como Coordenador.  
**Pós-condições:** Caso haja operações de adição, atualização ou exclusão, os cardápios semanais são atualizados no sistema.  

## Fluxo Principal

1. O coordenador seleciona a opção "Gerenciar Cardápio".
2. O sistema apresenta a tela “Gerenciar Cardápios” com abas funcionais (Visualizar, Adicionar, Atualizar e Deletar), permitindo ao coordenador alternar entre as operações disponíveis.
3. O sistema abre por padrão a aba "Visualizar".
4. O sistema exibe uma lista de cardápios organizados por período de datas.
5. Para cada cardápio, as informações são apresentadas por tipo de refeição, sendo: Cardápio do Lanche, Cardápio do Almoço e Cardápio do Jantar.
6. Cada tipo de refeição é organizado por data diária.
7. O Cardápio do Lanche é subdividido por turno, contemplando Manhã, Tarde e Noite, com os respectivos itens de cada período.

## Fluxos Alternativos

- **FA1 – Adicionar cardápio:**  
**Ponto de inserção:** Após o passo 2 do Fluxo Principal caso o Coordenador selecione a aba "Adicionar"
1. O sistema exibe os campos para informar a data inicial e a data final do cardápio.
2. O coordenador informa o período do cardápio.
3. O sistema gera automaticamente as datas correspondentes ao período informado.
4. Para cada data gerada, o sistema exibe os campos de seleção para os tipos de refeição:
   Lanche, Almoço e Jantar.
5. O coordenador seleciona os itens correspondentes a cada tipo de refeição.
6. O coordenador clica no botão "Adicionar".
7. O sistema valida os dados informados.
8. O sistema salva o novo cardápio.

- **FA2 – Atualizar cardápio:**  
**Ponto de inserção:** Após o passo 2 do Fluxo Principal caso o Coordenador selecione a aba "Atualizar"
1. O sistema exibe os campos para selecionar o cardápio e o dia desse cardápio. Sendo os campos respectivamente "Cardápio Escolhido" e "Data do cardápio".
2. O coordenador seleciona um cardápio existente.
3. O coordenado seleciona um dia do cardápio.
4. O sistema exibe os campos: Lanche da Manhã, Lanche da Tarde, Lanche da Noite, Almoço, Jantar.
5. O coordenador edita os campos selecionando outras opções de refeição.
6. O coordenador clica no botão "Atualizar".
7. O sistema valida os dados informados.
8. O sistema atualiza o cardápio.

- **FA3 – Deletar cardápio:**  
**Ponto de inserção:** Após o passo 2 do Fluxo Principal caso o Coordenador selecione a aba "Deletar"
1. O sistema exibe o campo para selecionar o cardápio.
2. O coordenador seleciona um cardápio existente.
3. O coordenador clica no botão "Deletar"
4. O sistema deleta o cardápio selecionado

## Fluxos De Exceção

- **FE1 – Dados incompletos:**  
    Caso o coordenador tente salvar ou atualizar um cardápio com campos obrigatórios em branco, o sistema exibirá uma mensagem de erro e não concluirá a operação.
1. Caso o coordenador tente salvar um cardápio com campos obrigatórios em branco, o sistema exibirá um aviso e não salvará o cardápio ou suas alterações.
