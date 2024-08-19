import pytest
from app.services import Services
from model.verbconj import Verb, Person, Tense
from db.mysql_repository import MysqlRepository

repo = MysqlRepository()
repo.create_tables()

def test_generate_conj():
    services = Services()
    verb = services.generate_conj('hablar')
    assert verb.get_conjugation(Tense.PRESENT, Person.FIRST_SINGULAR) == 'hablo'
