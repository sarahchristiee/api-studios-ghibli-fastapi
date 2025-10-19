from typing import Optional
from pydantic import BaseModel

# modelo de como os dados vão ser armazenados, o basemodel auxilia na validação de dados e aqui inserimos os atributos que vamos armazenar e o tipo deles
class Filme(BaseModel):
    id: Optional[int] = None
    titulo : str
    ano_lancamento : int
    diretor : str