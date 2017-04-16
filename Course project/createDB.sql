CREATE TABLE documents {
    passport        VARCHAR(10) NOT NULL, 
    faculty_code    INTEGER     NOT NULL,
	CONSTRAINT st PRIMARY KEY (passport, faculty_code)
};
CREATE TABLE faculty {
    faculty_code    INTEGER      PRIMARY KEY,
    name            VARCHAR(100) NOT NULL,
    university      VARCHAR(100) NOT NULL,
    city            VARCHAR(100),
    budget          INTEGER      NOT NULL,
    subject1        INTEGER      NOT NULL,
    subject2        INTEGER      NOT NULL,
    subject3        INTEGER      NOT NULL
};
CREATE TABLE subjects {
    subject_code    INTEGER      PRIMARY KEY,
    subject_name    VARCHAR(20)  NOT NULL UNIQUE
};
CREATE TABLE olympiads {
	code            INTEGER      PRIMARY KEY,
	name            VARCHAR(20)  NOT NULL UNIQUE,
	subject         INTEGER      NOT NULL,
	level           SMALLINT     NOT NULL CHECK (level >= 1 AND level <= 3) 
};
CREATE TABLE olymp_result {
	code            INTEGER      NOT NULL UNIQUE,
	passport        VARCHAR(10)  NOT NULL UNIQUE,
	degree          INTEGER      CHECK(degree >= 1 AND degree <= 3),
	CONSTRAINT st PRIMARY KEY (code, passport)
};
CREATE TABLE exams {
	passport        VARCHAR(10)  PRIMARY KEY,
	subject         INTEGER      NOT NULL,
	rating          INTEGER      NOT NULL CHECK(rating >= 0 AND rating <= 100)
};
CREATE TABLE pupils {
	passport        VARCHAR(10)  PRIMARY KEY,
	name            VARCHAR(100) NOT NULL UNIQUE,
	surname         VARCHAR(100) NOT NULL,
	midname        	VARCHAR(100),
	city            VARCHAR(100),
	gender          VARCHAR(1)   CHECK(gender == 'M' OR gender == 'F'),
	faculty_code    INTEGER
};

