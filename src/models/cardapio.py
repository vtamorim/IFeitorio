from datetime import datetime

class Cardapio:
    def __init__(self, id: int, di : datetime, df : datetime) -> None:
        self.set_id(id)
        self.set_di(di)
        self.set_df(df)
    
    def get_id(self) -> int:
        return self.__id 
    def get_di(self) -> str:
        return self.__di
    def get_df(self) -> list:
        return self.__df
    
    def set_id(self, id: int) -> None:
        if not isinstance(id, (int)): raise ValueError
        self.__id = id
    def set_di(self, di: datetime) -> None: 
        di = di.strip()
        if not isinstance(di, (datetime)): raise ValueError
        self.__di = di
    def set_df(self, df: datetime) -> None: 
        if not isinstance(df, (datetime)): raise ValueError
        self.__df = df

    def __str__(self) -> str:
           return f"{self.__id} - {self.__di} - {self.__df}"