import db.mysql_repository
from model.verbconj import Verb

class Services:

    def __init__(self):
        self.repo = db.mysql_repository.MysqlRepository()

    #Rete
    def generate_conj(self):
        verb = Verb()
        query = "SELECT tense, person, conjugation FROM verb_conjugations WHERE verb = 'hablar'"
        self.repo.cursor.execute(query)
        results = self.repo.cursor.fetchall()
        for tense_str, person_str, conjugation in results:
            tense = self.repo.map_tense({'tense': tense_str})
            person = self.repo.map_pronoun({'person': person_str})
            if tense and person:
                verb.add_conjugation(tense, person, conjugation)
        return verb

    def print_conj(self):
        conjugations = self.generate_conj().get_all_conjugations()
        for tense, persons in conjugations.items():
            print(f"Tense: {tense.name}")
            for person, conjugation in persons.items():
                print(f"  {person.name}: {conjugation}")

if __name__ == "__main__" :
    service = Services()
    service.print_conj()

