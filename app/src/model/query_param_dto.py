from pydantic import BaseModel
from typing import Optional

class QueryParamDTO(BaseModel):
    funcionario_id: Optional[str] = None    
    nome: Optional[str] = None    
    cpf: Optional[str] = None
    ativo: Optional[bool] = True
    estabelecimento_id: Optional[str] = None
