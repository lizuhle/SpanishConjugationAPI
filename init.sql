DROP DATABASE IF EXISTS spanishconj;
CREATE DATABASE spanishconj;
USE spanishconj;

DROP TABLE IF EXISTS verb_conjugations;
CREATE TABLE verb_conjugations (
    id INT NOT NULL AUTO_INCREMENT,
    verb VARCHAR(30),
    tense VARCHAR(30),
    person VARCHAR(50),
    conjugation VARCHAR(30),
    CONSTRAINT PRIMARY KEY (id)
);

INSERT INTO verb_conjugations
    (verb, tense, person, conjugation)

VALUES
('hablar', 'present', 'yo', 'hablo'),
('hablar', 'present', 'tú', 'hablas'),
('hablar', 'present', 'él, ella, usted', 'habla'),
('hablar', 'present', 'nosotros, nosotras', 'hablamos'),
('hablar', 'present', 'vosotros, vosotras', 'habláis'),
('hablar', 'present', 'ellos, ellas, ustedes', 'hablan'),
('hablar', 'present', 'vos', 'hablás');


