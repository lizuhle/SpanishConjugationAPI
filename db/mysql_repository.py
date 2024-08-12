import mysql.connector
from model.verbconj import Verb, Person, Tense


class MysqlRepository:

    def __init__(self):
        config = {
            'user': 'liz',
            'password': 'Spanconj123!',
            'host': 'localhost',
            'port': '3306',
            'database': 'spanishconj'
        }
        self.connection = mysql.connector.connect(**config)
        self.cursor = self.connection.cursor()

    def map_tense(self, entry: dict) -> Tense:
        tense_map = {
            "present": Tense.PRESENT,
        }
        tense = entry.get('tense', '').lower()
        tense_mapped = tense_map.get(tense)
        return tense_mapped

    def map_pronoun(self, entry: dict) -> Person:
        pronoun_map = {
            "yo": Person.FIRST_SINGULAR,
            "tú": Person.SECOND_SINGULAR,
            "él, ella, usted": Person.THIRD_SINGULAR,
            "nosotros, nosotras": Person.FIRST_PLURAL,
            "vosotros, vosotras": Person.SECOND_PLURAL,
            "ellos, ellas, ustedes": Person.THIRD_PLURAL,
            "vos": Person.VOS
        }
        pronoun = entry.get('person', '').lower()
        pronoun_mapped = pronoun_map.get(pronoun)
        return pronoun_mapped

    def create_tables(self):
        self.cursor.execute("""
                    CREATE TABLE IF NOT EXISTS verb_conjugations (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        verb VARCHAR(30),
                        tense VARCHAR(30),
                        person VARCHAR(50),
                        conjugation VARCHAR(30)
                    )
                """)
        self.connection.commit()

    # def __del__(self):
    #     self.cursor.close()
    #     self.connection.close()
