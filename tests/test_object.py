from model.verbconj import Verb, Person, Tense
import pytest

def test_tense_class():
    assert Tense.PRESENT == Tense(1)

def test_verb_add_conjugation():
    verb = Verb()
    verb.add_conjugation(Tense.PRESENT, Person.FIRST_SINGULAR, "hablo")
    assert verb.get_conjugation(Tense.PRESENT, Person.FIRST_SINGULAR) == "hablo"

