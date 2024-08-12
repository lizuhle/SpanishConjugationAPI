from flask import Flask, request, jsonify
from app.services import Services

app = Flask(__name__)
services = Services()

@app.route("/conjugate", methods=["GET"])
def get_conjugation():
    conjugations = services.generate_conj().get_all_conjugations()
    formatted_conj = {
        tense.name: {person.name: conjugation for person, conjugation in persons.items()}
        for tense, persons in conjugations.items()
    }
    return jsonify(formatted_conj)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
