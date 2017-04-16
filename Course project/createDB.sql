CREATE TABLE pupils {
	passport        VARCHAR(10)  PRIMARY KEY,
	name            VARCHAR(100) NOT NULL,
	surname         VARCHAR(100) NOT NULL,
	midname        	VARCHAR(100),
	city            VARCHAR(100),
	gender          VARCHAR(1)   CHECK(gender == 'M' OR gender == 'F'),
	faculty_code    INTEGER      REFERENCES faculty(faculty_code)
};

CREATE TABLE exams {
	passport        VARCHAR(10)  NOT NULL REFERENCES pupils(passport),
	subject         INTEGER      NOT NULL REFERENCES subjects(subject_code),
	rating          INTEGER      NOT NULL CHECK(rating >= 0 AND rating <= 100),
    CONSTRAINT member PRIMARY KEY (passport, subject)
};

CREATE TABLE olymp_result {
	code            INTEGER      NOT NULL REFERENCES olympiads(code),
	passport        VARCHAR(10)  NOT NULL REFERENCES pupils(passport),
	degree          INTEGER      CHECK(degree >= 1 AND degree <= 3),
	CONSTRAINT st PRIMARY KEY (code, passport)
};

CREATE TABLE olympiads {
	code            INTEGER      PRIMARY KEY,
	name            VARCHAR(20)  NOT NULL UNIQUE,
	subject         INTEGER      NOT NULL REFERENCES subjects(subject_code),
	level           SMALLINT     NOT NULL CHECK (level >= 1 AND level <= 3) 
};

CREATE TABLE documents {
    passport        VARCHAR(10) NOT NULL REFERENCES pupils(passport), 
    faculty_code    INTEGER     NOT NULL REFERENCES FACULTY(faculty_code),
	CONSTRAINT document PRIMARY KEY (passport, faculty_code)
};

CREATE TABLE faculty {
    faculty_code    INTEGER      PRIMARY KEY,
    name            VARCHAR(100) NOT NULL,
    university      VARCHAR(100) NOT NULL UNIQUE,
    city            VARCHAR(100),
    budget          INTEGER      NOT NULL,
    subject1        INTEGER      NOT NULL REFERENCES subjects(subject_code),
    subject2        INTEGER      NOT NULL REFERENCES subjects(subject_code),
    subject3        INTEGER      NOT NULL REFERENCES subjects(subject_code)
};

CREATE TABLE subjects {
    subject_code    INTEGER      PRIMARY KEY,
    subject_name    VARCHAR(20)  NOT NULL UNIQUE
};

