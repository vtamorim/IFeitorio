# CDU003 – Gerenciar Perfil

**Ator Primário:** Aluno e Coordenador.  
**Descrição:** Permite o usuario visualizar e alterar informações do seu perfil.  
**Pré-condições:** O usuário deve estar logado como aluno ou coordenador.  
**Pós-condições:** As informações do perfil do usuário serão atualizadas no sistema.

## Fluxo Principal

1. O usuario seleciona a opção "Meu Perfil".
2. O sistema exibe os campos de matricula (não editavel), nome e senha do usuario.  
2.1 Caso o usuário seja aluno, o sistema também exibe o campo de restrições alimentares.
3. O usuario edita as informações desejadas   
4. O usuario clica no botão "Atualizar"
5. O sistema valida as novas informações
6. O sistema atualiza as informações do usuario.

## Fluxo de exeção 
- **FE1 – Dados obrigatórios não preenchidos:** 
Caso o usuário tente salvar o perfil com algum campo obrigatório não preenchido, o sistema exibirá a mensagem de erro:
"Campos obrigatórios vazios, tente novamente", e a operação não será concluída.


