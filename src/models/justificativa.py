from .falta import Falta
from typing import Optional

class Justificativa:
    def __init__(self, id: int, falta: Falta, motivo: str, aprovada: Optional[bool] = None) -> None:
        self.set_id(id)
        self.set_falta(falta)
        self.set_motivo(motivo)
        self.set_aprovada(aprovada)
    
    def get_id(self) -> int:
        return self.__id
    def get_falta(self) -> Falta:
        return self.__falta
    def get_motivo(self) -> str:
        return self.__motivo
    def get_aprovada(self) -> Optional[bool]:
        return self.__aprovada

    def set_id(self, id: int) -> None:
        if not isinstance(id, int): raise ValueError("ID Inválido")

        self.__id = id
    def set_falta(self, falta: Falta) -> None:
        if not isinstance(falta, Falta): raise ValueError("Falta Inválida")

        self.__falta = falta
    def set_motivo(self, motivo: str) -> None:
        motivo = motivo.strip()
        if not isinstance(motivo, str): raise ValueError("Motivo Inválido")
        if motivo == "": raise ValueError("Motivo da Falta não pode ser Vazio!")

        self.__motivo = motivo
    def set_aprovada(self, aprovada: Optional[bool]) -> None:
        if aprovada is not None and not isinstance(aprovada, bool): raise ValueError("Aprovação Inválida")

        self.__aprovada = aprovada
    
    def __str__(self) -> str:
        aprovada_texto = f" | {self.__aprovada}" if self.__aprovada is not None is not None else " | Ainda Não Analisada"
        return f"Justificativa {self.__id} - Falta {self.__falta.get_id()}: {self.__motivo}{aprovada_texto}"
