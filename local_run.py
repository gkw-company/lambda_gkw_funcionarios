import os
import json
from types import SimpleNamespace
from app.lambda_function import lambda_handler


EVENT_FILE = "events/get_funcionario.json"
# EVENT_FILE = "events/post_funcionario.json"
#EVENT_FILE = "events/get_funcionario_query.json"
#EVENT_FILE = "events/patch_funcionario.json"

# Simula o contexto Lambda (você pode expandir se necessário)
class MockContext(SimpleNamespace):
    def __init__(self):
        super().__init__(
            function_name="local-test",
            function_version="1",
            invoked_function_arn="arn:aws:lambda:local",
            memory_limit_in_mb=128,
            aws_request_id="local-id",
            log_group_name="local-logs",
            log_stream_name="local-stream"
        )

if __name__ == "__main__":
    with open(EVENT_FILE, "r") as f:
        event = json.load(f)

    context = MockContext()
    response = lambda_handler(event, context)
    print("Response:", response)
