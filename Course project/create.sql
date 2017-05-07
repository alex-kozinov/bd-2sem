CREATE TABLE IF NOT EXISTS Subjects (
    subject_code    INTEGER      PRIMARY KEY,
    subject_name    VARCHAR(20)  NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS Faculty (
    faculty_code    INTEGER      PRIMARY KEY,
    name            VARCHAR(100) NOT NULL,
    university      VARCHAR(100) NOT NULL,
    city            VARCHAR(100),
    budget          INTEGER      NOT NULL,
    subject1        INTEGER      NOT NULL REFERENCES Subjects(subject_code),
    subject2        INTEGER      NOT NULL REFERENCES Subjects(subject_code),
    subject3        INTEGER      NOT NULL REFERENCES Subjects(subject_code)
);

CREATE TABLE IF NOT EXISTS Olympiads (
	code            INTEGER      PRIMARY KEY,
	name            VARCHAR(100) NOT NULL,
	subject         INTEGER      NOT NULL REFERENCES Subjects(subject_code),
	level           SMALLINT     NOT NULL CHECK (level >= 0 AND level <= 3) 
);

CREATE TABLE IF NOT EXISTS Pupils (
	passport        VARCHAR(10)  PRIMARY KEY,
	name            VARCHAR(100) NOT NULL,
	surname         VARCHAR(100) NOT NULL,
	midname        	VARCHAR(100),
	city            VARCHAR(100),
	gender          VARCHAR(1)   CHECK(gender == 'M' OR gender == 'F'),
	faculty_code    INTEGER      REFERENCES Faculty(faculty_code)
);

CREATE TABLE IF NOT EXISTS Exams (
	passport        VARCHAR(10)  NOT NULL REFERENCES Pupils(passport),
	subject         INTEGER      NOT NULL REFERENCES Subjects(subject_code),
	rating          INTEGER      NOT NULL CHECK(rating >= 0 AND rating <= 100),
    CONSTRAINT member PRIMARY KEY (passport, subject)
);

CREATE TABLE IF NOT EXISTS Olymp_result (
	code            INTEGER      NOT NULL REFERENCES Olympiads(code),
	passport        VARCHAR(10)  NOT NULL REFERENCES Pupils(passport),
	degree          INTEGER      CHECK(degree >= 1 AND degree <= 3),
	CONSTRAINT st PRIMARY KEY (code, passport)
);

CREATE TABLE IF NOT EXISTS Documents (
    passport        VARCHAR(10) NOT NULL REFERENCES Pupils(passport), 
    faculty_code    INTEGER     NOT NULL REFERENCES Faculty(faculty_code),
	CONSTRAINT document PRIMARY KEY (passport, faculty_code)
);
