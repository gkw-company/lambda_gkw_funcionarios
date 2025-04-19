from peewee import *
from app.src.util.db_connect import db
import uuid

class BaseModel(Model):
    class Meta:
        database = db
        

class FuncionarioModel(BaseModel):
    funcionario_id = UUIDField(primary_key=True, default=uuid.uuid4)
    nome = CharField()
    email = CharField()
    celular = CharField()
    cpf = CharField()
    ativo = BooleanField(default=True)
    estabelecimento_id = CharField(null=True)
    
    class Meta:
        table_name = "Funcionario"
