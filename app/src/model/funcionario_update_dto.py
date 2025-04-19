from pydantic import BaseModel
from typing import Optional

class FuncionarioUpdateDTO(BaseModel):
    nome: Optional[str] = None
    email: Optional[str] = None
    celular: Optional[str] = None
    cpf: Optional[str] = None
    ativo: Optional[bool] = None
    estabelecimento_id: Optional[str] = None
