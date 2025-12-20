# CDU019 – Gerenciar faltas dos alunos

**Ator Primário:** Coordenador.  
**Descrição:** Permite o coordenador adicionar ou editar as faltas dos alunos.  
**Pré-condições:** O usuário deve estar cadastrado como coordenador.  
**Pós-condições:** Algumas faltas podem ser adicionadas, modificadas ou excluídas.  

## Fluxo Principal

1. O coordenador acessa o sistema com login de coordenador.
2. O coordenador seleciona a opção "Gerenciar Faltas".
3. O sistema exibe um painel com as faltas dos alunos e as opções para enviar, editar ou excluir faltas.
4. O coordenador pode selecionar a opção de adicionar falta e inserir os dados da falta ou selecionar uma falta já existente para modificá-la ou excluí-la.

## Fluxos De Exceção

- **FE1 – Dados incompletos/incorretos:**  
6. Caso o coordenador tente cadastrar ou modificar uma falta com campos obrigatórios em branco ou com dados incorretos, o sistema exibirá um aviso e não salvará as alterações.
