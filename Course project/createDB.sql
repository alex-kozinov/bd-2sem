CREATE TABLE documents {
    passport        VARCHAR(10) NOT NULL, 
    faculty_code    INTEGER NOT NULL
};
CREATE TABLE faculty {
    faculty_code    INTEGER PRIMARY KEY,
    name            VARCHAR(100) NOT NULL,
    university,     VARCHAR(100) NOT NULL,
    city,           VARCHAR(100),
    budget,         INTEGER NOT NULL,
    subject1,       VARCHAR(20) NOT NULL,
    subject2,       VARCHAR(20) NOT NULL,
    subject3        VARCHAR(20) NOT NULL
}
CREATE TABLE subjects {
    subject_code,   INTEGER NOT NULL UNIQUE
    subject_name    VARCHAR(20) NOT NULL UNIQUE,
    CONSTRAINT subj PRIMARY KEY(subject_code, subject_name)
}

