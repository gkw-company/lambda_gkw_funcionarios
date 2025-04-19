from app.src.model.funcionario_dto import FuncionarioDTO
from app.src.model.funcionario_model import FuncionarioModel
from app.src.model.funcionario_update_dto import FuncionarioUpdateDTO
from app.src.model.query_param_dto import QueryParamDTO
from app.src.repository.funcionario_repository import FuncionarioRepository
from aws_lambda_powertools import Logger
#import json

repository = FuncionarioRepository()
logger = Logger()


class FuncionarioService():
    def cadastrar_funcionario(self, funcionario: FuncionarioDTO) -> dict:
        
        try:
            return repository.cadastrar_funcionario(funcionario)
        except Exception as e:
            raise Exception(f"Erro ao cadastrar funcionário: {str(e)}")
    
    def atualizar_funcionario(self, funcionario_id: str, funcionario: FuncionarioUpdateDTO) -> dict:
        try:
            return repository.atualizar_funcionario(funcionario_id=funcionario_id, funcionario_dto=funcionario)
        except Exception as e:
            raise Exception(f"Erro ao atualizar funcionário: {str(e)}")
        
    def consultar_funcionarios(self):
        try:
            return repository.consultar_funcionarios()
        except Exception as e:
            raise Exception(f"Erro ao consultar funcionários cadastrados: {str(e)}")
        
    def consultar_funcionarios_query(self, queryParam: QueryParamDTO):
        try:
            return repository.consultar_funcionarios_query(queryParam)
        except Exception as e:
            raise Exception(f"Erro ao consultar funcionários cadastrados: {str(e)}")