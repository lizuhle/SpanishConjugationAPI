from flask import Flask, request, jsonify
from flask_cors import CORS
from app.services import Services

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app)
services = Services()

@app.route('/')
def doc() -> str:
    with open("app/spanishconjugation.html", "r") as f:
        return f.read()

@app.route("/conjugate", methods=["POST"])
def conjugate_verb():
    data = request.get_json()
    inf_verb = data.get('verb')

    if not inf_verb:
        return jsonify({"error": "No verb provided"}), 400
    verb = services.generate_conj(inf_verb)
    conjugations = verb.get_all_conjugations()

    formatted_conjugations = {}
    for tense, persons in conjugations.items():
        formatted_conjugations[tense.name] = {person.name: conjugation for person, conjugation in persons.items()}

    return jsonify(formatted_conjugations)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
