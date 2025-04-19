from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class FuncionarioDTO(BaseModel):
    nome: str
    email: str
    celular: str
    cpf: str
    ativo: Optional[bool] = True
    estabelecimento_id: Optional[str] = None

class FuncionarioResponseDTO(FuncionarioDTO):
    funcionario_id: UUID
