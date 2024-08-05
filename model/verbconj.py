from enum import Enum


class Tense(Enum):
    PRESENT = 1
    PRETERITE = 2
    IMPERFECT = 3
    FUTURE = 4
    CONDITIONAL = 5


class Person(Enum):
    FIRST_SINGULAR = 1
    SECOND_SINGULAR = 2
    THIRD_SINGULAR = 3
    FIRST_PLURAL = 4
    SECOND_PLURAL = 5
    THIRD_PLURAL = 6
    VOS = 7


class Verb:
    def __init__(self, infinitive):
        self.infinitive = infinitive
        self.conjugations = {}



    def add_conjugation(self, tense: Tense, person: Person, conjugation: str):
        if tense not in self.conjugations:
            self.conjugations[tense] = {}
        self.conjugations[tense][person] = conjugation

    def get_conjugation(self, tense: Tense, person: Person) -> str:
        return self.conjugations.get(tense, {}).get(person, "")

    def get_all_conjugations(self):
        return self.conjugations
