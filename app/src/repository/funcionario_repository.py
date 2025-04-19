from app.src.model.funcionario_dto import FuncionarioDTO
from app.src.model.funcionario_model import FuncionarioModel
from aws_lambda_powertools import Logger
from peewee import OperationalError
from app.src.model.query_param_dto import QueryParamDTO
from app.src.util.db_connect import db

logger = Logger()

class FuncionarioRepository():
    
    def cadastrar_funcionario(self, funcionario: FuncionarioDTO) -> dict:
        try:
            
            with db.connection_context():
                funcionario = FuncionarioModel.create(**funcionario.model_dump())

            return {
                "message": "Funcionário criado com sucesso",
                "funcionario_id": str(funcionario.funcionario_id)
            }

        except OperationalError as e:
            logger.error(e)
        except Exception as e:
            logger.error(e)
            raise Exception(f"Erro ao salvar funcionário: {str(e)}")
        finally:
            if not db.is_closed():
                db.close()

    def atualizar_funcionario(self, funcionario_id: str, funcionario_dto: FuncionarioDTO) -> dict:
        try:
            dados = funcionario_dto.model_dump(exclude_unset=True)

            dados.pop("funcionario_id", None)

            with db.connection_context():
                linhas_afetadas = (
                    FuncionarioModel
                    .update(**dados)
                    .where(FuncionarioModel.funcionario_id == funcionario_id)
                    .execute()
                )

                if not linhas_afetadas:
                    raise Exception("Funcionário não encontrado para atualização.")

            return {
                "message": "Funcionário atualizado com sucesso",
                "funcionario_id": funcionario_id
            }

        except OperationalError as e:
            logger.error(e)
            raise Exception("Erro de conexão ao atualizar funcionário.")
        except Exception as e:
            logger.error(e)
            raise Exception(f"Erro ao atualizar funcionário: {e}")
        finally:
            if not db.is_closed():
                db.close()
                
    def consultar_funcionarios(self):
        try:
            
            with db.connection_context():
                query = FuncionarioModel.select().dicts()
                return list(query)
            
        except OperationalError as e:
            logger.error(e)
        except Exception as e:
            logger.error(e)
            raise Exception(f"Erro ao salvar funcionário: {str(e)}")
        finally:
            if not db.is_closed():
                db.close()
    
    def consultar_funcionarios_query(self, queryParam: QueryParamDTO):
        try:
            with db.connection_context():
                query = FuncionarioModel.select()

                if queryParam.funcionario_id:
                    query = query.where(FuncionarioModel.funcionario_id == queryParam.funcionario_id)
                if queryParam.nome:
                    query = query.where(FuncionarioModel.nome.contains(queryParam.nome))
                if queryParam.cpf:
                    query = query.where(FuncionarioModel.cpf == queryParam.cpf)
                if queryParam.estabelecimento_id:
                    query = query.where(
                        FuncionarioModel.estabelecimento_id == queryParam.estabelecimento_id
                    )

                return list(query.dicts())

        except OperationalError as e:
            logger.error(e)
            raise Exception("Erro de conexão ao buscar funcionários")
        except Exception as e:
            logger.error(e)
            raise Exception(f"Erro ao buscar funcionários: {e}")
        finally:
            if not db.is_closed():
                db.close()
            