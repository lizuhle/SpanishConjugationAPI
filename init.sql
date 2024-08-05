CREATE DATABASE spanishconj;
ALTER DATABASE spanishconj CHARACTER SET utf8mb4 COLLATE utf8_unicode_ci;
USE spanishconj;

CREATE TABLE verb_conjugations (
    id INT NOT NULL AUTO_INCREMENT,
    verb NVARCHAR(30)
    tense NVARCHAR(30)
    person NVARCHAR(20)
    conjugation NVARCHAR(30)
    CONSTRAINT PRIMARY KEY (id)
);

INSERT INTO verb_conjugations
    (verb, tense, person, conjugation)


