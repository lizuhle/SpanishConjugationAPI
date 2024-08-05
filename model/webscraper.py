import requests
from bs4 import BeautifulSoup
from model.verbconj import Verb, Tense, Person


def scrape_conjugations(verb):
    url = f"https://www.wordreference.com/conj/esverbs.aspx?v={verb}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table', class_='neoConj active')
    conjugations = []

    for row in table.find_all('tr'):
        pronoun = row.find('th', scope='row')
        conjugation = row.find('td')
        if pronoun and conjugation:
            conjugations.append((pronoun.get_text(strip=True), conjugation.get_text(strip=True)))
    return conjugations

    # pronoun_to_person = {
    #     "yo": Person.FIRST_SINGULAR,
    #     "tú": Person.SECOND_SINGULAR,
    #     "él, ella, usted": Person.THIRD_SINGULAR,
    #     "nosotros, nosotras": Person.FIRST_PLURAL,
    #     "vosotros, vosotras": Person.SECOND_PLURAL,
    #     "ellos, ellas, ustedes": Person.THIRD_PLURAL
    # }
    #
    # tense_map = {
    #     "presente": Tense.PRESENT,
    #     "preterito": Tense.PRETERITE,
    #     "imperfecto": Tense.IMPERFECT,
    #     "futuro": Tense.FUTURE,
    #     "condicional": Tense.CONDITIONAL
    # }

if __name__ == "__main__" :
    scrape_conjugations("hablar")