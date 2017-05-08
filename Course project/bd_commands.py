import sqlite3
import os

def cls():
    os.system(['clear','cls'][os.name == 'nt'])

class Pupil(object):
    def __init__(self):
        self.passport = "Null"
        self.name = "Null"
        self.surname = "Null"
        self.midname = "Null"
        self.city = "Null"
        self.gender = "Null"
        self.faculty_code = "Null"

    def assign_data(self, data):
        self.passport = data[0]
        self.name = data[1]
        self.surname = data[2]
        self.midname = data[3]
        self.city = data[4]
        self.gender = data[5]
        self.faculty_code = data[6]

    def insert(self, cursor):
        query_table(cursor, "INSERT INTO Pupils" \
                         "(passport, name, surname, midname, city, gender, faculty_code)" \
                         "VALUES (?, ?, ?, ?, ?, ?, ?)",
                    (self.passport, self.name, self.surname, self.midname, self.city, self.gender, self.faculty_code),
                    "Incorrect Pupil's data: ")

    def read_passport(self):
        print("Серия: ")
        self.passport = input()
        print("Номер: ")
        self.passport = self.passport + input()

    def read_other_data(self):
        print("Введите Имя: ")
        self.name = input()
        print("Введите Фамилию: ")
        self.surname = input()
        print("Введите Отчество: ")
        self.midname = input()
        if self.midname == "":
            self.midname = "NULL"
        print("Введите город: ")
        self.city = input()
        print("Введите пол (M/F): ")
        self.gender = input()

def create_connection(db_file):
    conn = sqlite3.connect(db_file)
    return conn


def query_table(cursor, query_sql, params, error_text):
    try:
        if params == None:
            cursor.execute(query_sql)
        else:
            cursor.execute(query_sql, params)
    except sqlite3.Error as e:
        print(error_text, e.args[0])




def query_from_file(cursor, file_name, commands_type):
    with open(file_name) as file_query:
        s = file_query.read()
        for c in s.split(commands_type):
            if c == "":
                continue
            c = commands_type + c
            query_table(cursor, c, None, "Wrong command format in file")
            for i in cursor:
                print(str(i))


