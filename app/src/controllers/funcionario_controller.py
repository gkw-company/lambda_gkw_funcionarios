from aws_lambda_powertools.event_handler import APIGatewayRestResolver
from aws_lambda_powertools import Logger, Tracer
from aws_lambda_powertools.event_handler.api_gateway import Router
from pydantic import ValidationError
from app.src.model.funcionario_dto import FuncionarioDTO
from app.src.model.funcionario_update_dto import FuncionarioUpdateDTO
from app.src.model.query_param_dto import QueryParamDTO
from app.src.services.funcionario_service import FuncionarioService
from build.aws_lambda_powertools.event_handler.exceptions import BadRequestError

service = FuncionarioService()
resolver = APIGatewayRestResolver()
tracer = Tracer()
logger = Logger()
router = Router()


@router.post("/funcionarios")
@tracer.capture_method(capture_response=True)
def postFuncionarios(input_model: FuncionarioDTO):

    try:
    
        logger.info(input_model)
        response = service.cadastrar_funcionario(input_model)

        return {
            "statusCode": 201,
            "body": {
                "message": "Funcionário cadastrado com sucesso",
                "funcionario": response.get("funcionario_id")
            }
        }

    except Exception as e:
        logger.error(f"Erro ao postFuncionarios funcionário: {str(e)}")
        return {
            "statusCode": 500,
            "body": {
                "message": "Erro ao cadastrar funcionário",
                "error": str(e)
            }
        }

@router.patch("/funcionarios/<funcionario_id>")
def atualizar_funcionario(funcionario_id: str, input_model: FuncionarioUpdateDTO):
    try:

        resultado = service.atualizar_funcionario(funcionario_id, input_model)
        return {
            "statusCode": 200,
            "body": resultado
        }
        
    except Exception as e:
        logger.error(f"Erro ao atualizar o funcionário: {str(e)}")
        return {
            "statusCode": 500,
            "body": {
                "message": "Erro ao atualizar funcionário",
                "error": str(e)
            }
        }

@router.get("/funcionarios/search")
@tracer.capture_method(capture_response=True)
def consultar_funcionarios_query():
    params = router.current_event.query_string_parameters or {}
    try:
        query_params = QueryParamDTO.model_validate(params)
    except ValidationError as exc:
        raise BadRequestError(exc.json())
    
    resultados = service.consultar_funcionarios_query(query_params)

    if not resultados:
        return {"statusCode": 204, "body": ""}

    return {
        "statusCode": 200,
        "body": {"funcionarios": resultados}
    }
    
@router.get("/funcionarios")
@tracer.capture_method(capture_response=True)
def consultar_funcionarios_query():
    try:
    
        resultados = service.consultar_funcionarios()

        if not resultados:
            return {"statusCode": 204, "body": ""}

        return {
            "statusCode": 200,
            "body": {"funcionarios": resultados}
        }

    except Exception as e:
        logger.error(f"Erro ao consultar funcionários: {str(e)}")
        return {
            "statusCode": 500,
            "body": {
                "message": "Erro ao consultar funcionários",
                "error": str(e)
            }
        }   