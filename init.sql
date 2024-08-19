CREATE DATABASE spanishconj;
ALTER DATABASE spanishconj CHARACTER SET utf8mb4 COLLATE utf8_unicode_ci;
USE spanishconj;

CREATE TABLE verb_conjugations (
    id INT NOT NULL AUTO_INCREMENT,
    verb VARCHAR(30),
    tense VARCHAR(30),
    person VARCHAR(20),
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


