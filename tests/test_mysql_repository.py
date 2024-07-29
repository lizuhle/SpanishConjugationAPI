import pytest
from db.mysql_repository import *
from model.verbconj import *

def setup_db():
    repo = MysqlRepository()
    repo.create_tables()
    yield repo


def test_get_verb_by_infinitive(setup_db):
    repo = setup_db

    # Create a test verb and add conjugations
    verb = Verb('hablar')
    verb.add_conjugation(Tense.PRESENT, Person.FIRST_SINGULAR, 'hablo')
    verb.add_conjugation(Tense.PRESENT, Person.SECOND_SINGULAR, 'hablas')

    # Insert the verb into the database
    repo.insert_verb(verb)

    # Retrieve the verb by its infinitive
    retrieved_verb = repo.get_verb_by_infinitive('hablar')

    # Assert that the verb was retrieved correctly
    assert retrieved_verb is not None
    assert retrieved_verb.infinitive == 'hablar'
    assert retrieved_verb.get_conjugation(Tense.PRESENT, Person.FIRST_SINGULAR) == 'hablo'
    assert retrieved_verb.get_conjugation(Tense.PRESENT, Person.SECOND_SINGULAR) == 'hablas'
