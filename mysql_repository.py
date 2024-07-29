import mysql.connector
from model.verbconj import *


class MysqlRepository:

    def __init__(self):
        super().__init__()
        config = {
            'user': 'root',
            'password': 'root',
            'host': 'localhost',
            'port': '32000',
            'database': 'spanishconj'
        }
        self.connection = mysql.connector.connect(**config)
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.connection.close()

    def create_tables(self):
        self.cursor.execute("""
                    CREATE TABLE IF NOT EXISTS verbs (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        infinitive VARCHAR(50) NOT NULL
                    )
                """)
        self.cursor.execute("""
                    CREATE TABLE IF NOT EXISTS spanishconj (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        verb_id INT,
                        tense INT,
                        person INT,
                        conjugation VARCHAR(50),
                        FOREIGN KEY (verb_id) REFERENCES verbs(id)
                    )
                """)
        self.connection.commit()

    def insert_verb(self, verb: Verb):
        sql = "INSERT INTO verbs (infinitive) VALUES (%s)"
        self.cursor.execute(sql, (verb.infinitive,))
        verb_id = self.cursor.lastrowid
        for tense, persons in verb.get_all_conjugations().items():
            for person, conjugation in persons.items():
                sql = "INSERT INTO conjugations (verb_id, tense, person, conjugation) VALUES (%s, %s, %s, %s)"
                self.cursor.execute(sql, (verb_id, tense.value, person.value, conjugation))
        self.connection.commit()

    def get_verb_by_infinitive(self, infinitive: str) -> Verb:
        sql = "SELECT id FROM verbs WHERE infinitive = %s"
        self.cursor.execute(sql, (infinitive,))
        result = self.cursor.fetchone()
        if not result:
            return None
        verb_id = result[0]
        verb = Verb(infinitive)
        sql = "SELECT tense, person, conjugation FROM conjugations WHERE verb_id = %s"
        self.cursor.execute(sql, (verb_id,))
        for tense, person, conjugation in self.cursor.fetchall():
            verb.add_conjugation(Tense(tense), Person(person), conjugation)
        return verb

