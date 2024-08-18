import pytest
import mysql.connector
from model.verbconj import Verb, Person, Tense
from db.mysql_repository import MysqlRepository  # Adjust import according to your structure


@pytest.fixture(scope="module")
def mysql_repository():
    repo = MysqlRepository()
    repo.create_tables()
    yield repo
    repo.cursor.execute("DROP TABLE IF EXISTS verb_conjugations")
    repo.connection.close()


def test_insert_conjugations(mysql_repository):
    mysql_repository.insert_conjugations()

    mysql_repository.cursor.execute("SELECT * FROM verb_conjugations WHERE verb = 'hablar'")
    results = mysql_repository.cursor.fetchall()

    expected_results = [
        (1, 'hablar', 'present', 'yo', 'hablo'),
        (2, 'hablar', 'present', 'tú', 'hablas'),
        (3, 'hablar', 'present', 'él, ella, usted', 'habla'),
        (4, 'hablar', 'present', 'nosotros, nosotras', 'hablamos'),
        (5, 'hablar', 'present', 'vosotros, vosotras', 'habláis'),
        (6, 'hablar', 'present', 'ellos, ellas, ustedes', 'hablan'),
        (7, 'hablar', 'present', 'vos', 'hablás'),
    ]

    assert len(results) == len(expected_results)