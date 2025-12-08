from datetime import datetime
class Justificativa:
    def __init__(self, id: int, d: datetime, m: str,) -> None:
        self.set_id(id)
        self.set_data(d)
        self.set_motivo(m)
        self.__aluno_matricula = None
        self.__refeicao_id = None
    
    def get_id(self) -> int:
        return self.__id 
    def get_data(self) -> datetime:
        return self.__data
    def get_motivo(self) -> str:
        return self.__motivo
    def get_alu_mat(self) -> str:
        return self.__aluno_matricula
    def get_ref_id(self) -> int:
        return self.__refeicao_id
    
    def set_id(self, id: int) -> None:
        if not isinstance(id, (int)): raise ValueError
        self.__id = id
    def set_data(self, d: datetime) -> None: 
        if not isinstance(d, (datetime)): raise ValueError
        self.__data = d
    def set_motivo(self, m: str) -> None: 
        m = m.strip() # retira "espaços" dos lados da string
        if m == "": raise ValueError
        self.__motivo = m
    def set_alu_mat(self, am: str) -> None: 
        if am == "": raise ValueError
        self.__aluno_matricula = am
    def set_refeicao_id(self, ri: int) -> None: 
        if not isinstance(ri, (int)): raise ValueError
        self.__refeicao_id = ri

    def __str__(self) -> str:
           return f"{self.__id} - {self.__data} - {self.__motivo} - {self.__aluno_matricula} - {self.__refeicao_id}"