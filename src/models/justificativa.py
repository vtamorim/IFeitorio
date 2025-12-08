from .coordenador import Coordenador
from .falta import Falta
from typing import Optional

class Justificativa:
    def __init__(self, id: int, falta: Falta, motivo: str, aprovada: Optional[bool] = None, coordenador: Optional[Coordenador] = None) -> None:
        self.set_id(id)
        self.set_falta(falta)
        self.set_motivo(motivo)
        self.set_aprovada(aprovada)
        self.set_coordenador(coordenador)
    
    def get_id(self) -> int:
        return self.__id
    def get_falta(self) -> Falta:
        return self.__falta
    def get_motivo(self) -> str:
        return self.__motivo
    def get_aprovada(self) -> Optional[bool]:
        return self.__aprovada
    def get_coordenador(self) -> Optional[Coordenador]:
        return self.__coordenador

    def set_id(self, id: int) -> None:
        if not isinstance(id, int): raise ValueError

        self.__id = id
    def set_falta(self, falta: Falta) -> None:
        if not isinstance(falta, Falta): raise ValueError

        self.__falta = falta
    def set_motivo(self, motivo: str) -> None:
        if not isinstance(motivo, str): raise ValueError

        self.__motivo = motivo
    def set_aprovada(self, aprovada: bool) -> None:
        if not isinstance(aprovada, bool): raise ValueError

        self.__aprovada = aprovada
    def set_coordenador(self, coordenador: Coordenador) -> None:
        if not isinstance(coordenador, Coordenador): raise ValueError

        self.__coordenador = coordenador
    
    def __str__(self) -> None:
        aprovada_texto = f" | {self.__aprovada} - {self.__coordenador.get_nome()}" if self.__aprovada is not None and self.__coordenador is not None else " | Ainda Não Analisada"
        return f"Justificativa {self.__id} - Falta {self.__falta.get_id()}: {self.__motivo}{aprovada_texto}"
