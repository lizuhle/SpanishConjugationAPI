import requests
import mysql.connector
from bs4 import BeautifulSoup


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

def insert_conjugations(conjugations):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='spanishconj'
        )
        cursor = connection.cursor()

        insert_conj = """
        INSERT INTO verb_conjugations (verb, tense, person, conjugation)
        VALUES (%s, %s, %s, %s)
        """

        for conjugation in conjugations:
            verb = "hablar"
            tense = "present"
            person = conjugation[0]
            conjugation_form = conjugation[1]
            cursor.execute(insert_conj, (verb, tense, person, conjugation_form))
        connection.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


if __name__ == "__main__" :
    verb = "hablar"
    conjugations = scrape_conjugations(verb)
    insert_conjugations(conjugations)

