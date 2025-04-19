from peewee import MySQLDatabase

db = MySQLDatabase(
    database="sistema_agendamento",
    user="root",
    password="root123",
    host="localhost",
    port=3307
)