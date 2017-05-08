import sqlite3
import os

def cls():
    os.system(['clear','cls'][os.name == 'nt'])

def read_str():
    ans = input(">")
    while ans == "":
        ans = input(">")
    return ans;

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

    def init_with_passport(self, cursor):
        query_table(cursor, "SELECT * FROM Pupils WHERE passport = " + str(self.passport), \
                    None, "Incorrect passport ")

        res = cursor.fetchall()
        if len(res) == 0:
            return 0

        self.assign_data(res[0])
        return 1

    def insert(self, cursor):
        query_table(cursor, "INSERT INTO Pupils" \
                         "(passport, name, surname, midname, city, gender, faculty_code)" \
                         "VALUES (?, ?, ?, ?, ?, ?, ?)",
                    (self.passport, self.name, self.surname, self.midname, self.city, self.gender, self.faculty_code),
                    "Incorrect Pupil's data: ")

    def read_passport(self):
        print("Серия: ")
        self.passport = read_str()
        print("Номер: ")
        self.passport = self.passport + read_str()

    def read_name(self):
        print("Введите Имя: ")
        self.name = read_str()

    def read_surname(self):
        print("Введите Фамилию: ")
        self.surname = read_str()

    def read_midname(self):
        print("Введите Отчество: ")
        self.midname = input(">")
        if self.midname == "":
            self.midname = "NULL"

    def read_city(self):
        print("Введите Город: ")
        self.city = input(">")
        if self.city == "":
            self.city = "NULL"

    def read_gender(self):
        print("Введите ваш пол (M/F): ")
        self.gender = read_str()
        while self.gender != "M" and self.gender != "F":
            self.gender = read_str()

    def read_other_data(self):
        self.read_name()
        self.read_surname()
        self.read_midname()
        self.read_city()
        self.read_gender()

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


