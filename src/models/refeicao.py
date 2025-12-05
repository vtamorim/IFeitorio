from datetime import datetime

class Refeicao:
    def __init__(self, id: int, n: str, d: str, t: str, dt: datetime) -> None:
        self.set_id(id)
        self.set_nome(n)
        self.set_descricao(d)
        self.set_tipo(t)
        self.set_data(dt)
    
    def get_id(self) -> int:
        return self.__id # Terminar dps