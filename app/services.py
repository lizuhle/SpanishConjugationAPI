import db.mysql_repository
from model.verbconj import Verb

class Services:

    def __init__(self):
        self.repo = db.mysql_repository.MysqlRepository()

    def generate_conj(self, inf_verb: str):
        verb = Verb()
        query = "SELECT tense, person, conjugation FROM verb_conjugations WHERE verb = %s"
        self.repo.cursor.execute(query, (inf_verb,))
        results = self.repo.cursor.fetchall()

        for tense_str, person_str, conjugation in results:
            tense = self.repo.map_tense({'tense': tense_str})
            person = self.repo.map_pronoun({'person': person_str})
            if tense and person:
                verb.add_conjugation(tense, person, conjugation)

        conjugations = verb.get_all_conjugations()
        for tense, persons in conjugations.items():
            print(f"Tense: {tense.name}")
            for person, conjugation in persons.items():
                print(f"  {person.name}: {conjugation}")

        return verb


if __name__ == "__main__" :
    service = Services()
    verb_conj = service.generate_conj('hablar')


