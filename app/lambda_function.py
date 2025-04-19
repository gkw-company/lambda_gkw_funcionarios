
from aws_lambda_powertools.utilities.typing import LambdaContext
from aws_lambda_powertools import Logger, Tracer
from aws_lambda_powertools.event_handler import APIGatewayRestResolver
from aws_lambda_powertools.event_handler import CORSConfig
import app.src.controllers.funcionario_controller as funcionarioController

logger = Logger()
tracer = Tracer()
app = APIGatewayRestResolver(
    cors=CORSConfig(),
    enable_validation=True,
    debug=True
)
app.include_router(funcionarioController.router)


@logger.inject_lambda_context()
@tracer.capture_lambda_handler
def lambda_handler(event: dict, context: LambdaContext) -> dict:
    return app.resolve(event, context)
