from views import View

class UI:
    """Programa de Terminal que realiza o CRUD do 'Coordenador'."""
    @staticmethod
    def menu() -> int:
        print("1 - Adicionar Coordenador\n2 - Listar Coordenadores\n3 - Listar Coordenador por Matrícula\n4 - Atualizar Coordenador\n5 - Excluir Coordenador\n6 - Sair do Programa")
        opcao = int(input("- Selecione uma opção acima: "))
        return opcao
    
    @staticmethod
    def main() -> None:
        while True:
            opcao = UI.menu()

            match opcao:
                case 1: UI.add_coord()
                case 2: UI.get_all_coord()
                case 3: UI.get_coord()
                case 4: UI.update_coord()
                case 5: UI.delete_coord()
                case 6:
                    print("Saindo do Program...")
                    break
                case _: print("Opção Inválida")
    
    @staticmethod
    def add_coord() -> None:
        mat = input("- Matrícula: ")
        nome = input("- Nome: ")
        senha = input("- Senha: ")
        View.coordenador_add(mat, nome, senha)
        print("Adicionado com Sucesso!")
    
    @staticmethod
    def get_all_coord() -> None:
        coords = View.coordenador_get_all()

        for c in coords:
            print(c)

    @staticmethod
    def get_coord() -> None:
        mat = input("- Matrícula: ")
        print(View.coordenador_get_matricula(mat))
    
    @staticmethod
    def update_coord() -> None:
        mat = input("- Matrícula: ")
        nome = input("- Novo Nome: ")
        senha = input("- Nova Senha: ")
        View.coordenador_update(mat, nome, senha)
        print("Atualizado com Sucesso!")
    
    @staticmethod
    def delete_coord() -> None:
        mat = input("- Matrícula: ")
        View.coordenador_delete(mat)
        print("Deletado com Sucesso!")

if __name__ == "__main__":
    UI.main()
