from datetime import datetime
class Justificativa:
    def __init__(self, id: int, d: datetime, m: str, am: str, ri: int) -> None:
        self.set_id(id)
        self.set_data(d)
        self.set_motivo(m)
        self.set_alu_mat(am)
        self.set_refeicao_id(ri)
    
    def get_id(self) -> int:
        return self.__id 
    def get_data(self) -> datetime:
        return self.__data
    def get_motivo(self) -> str:
        return self.__motivo
    def get_alu_mat(self) -> str:
        return self.__alu_mat
    def get_ref_id(self) -> int:
        return self.__ref_id
    
    def set_id(self, id: int) -> None:
        if not isinstance(id, (int)): raise ValueError
        self.__id = id
    def set_matricula(self, matricula: str) -> None: 
        if matricula == "": raise ValueError
        self.__matricula = matricula
    def set_nome(self, nome: str) -> None: 
        nome = nome.strip() # retira "espaços" dos lados da string
        if nome == "": raise ValueError
        self.__nome = nome
    def set_senha(self, senha: str) -> None: 
        senha = senha.strip() # retira "espaços" dos lados da string
        if senha == "": raise ValueError
        self.__senha = senha
    def set_restricoes(self, restricoes: list) -> None: 
        if not isinstance(restricoes, (list)): raise ValueError
        self.__restricoes = restricoes

    def __str__(self) -> str:
           return f"{self.__id} - {self.__nome} - {self.__matricula} - {self.__senha} - {self.__restricoes}"