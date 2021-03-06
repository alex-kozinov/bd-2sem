from simple import *
import sqlite3

class Pupil(object):
    def __init__(self):
        self.passport = "NULL"
        self.name = "NULL"
        self.surname = "NULL"
        self.midname = "NULL"
        self.city = "NULL"
        self.gender = "NULL"
        self.faculty_code = "NULL"

    def assign_data(self, data):
        self.passport = to_sql_format(data[0])
        self.name = to_sql_format(data[1])
        self.surname = to_sql_format(data[2])
        self.midname = to_sql_format(data[3])
        self.city = to_sql_format(data[4])
        self.gender = to_sql_format(data[5])
        self.faculty_code = to_sql_format(data[6])

    def init_with_passport(self, cursor):
        query_table(cursor, "SELECT * FROM Pupils WHERE passport = " + str(self.passport), \
                    None, "Incorrect passport ")

        res = cursor.fetchall()
        if len(res) == 0:
            return 0

        self.assign_data(res[0])
        return 1

    def erase(self, cursor):
        query_table(cursor, "DELETE " \
                            "FROM Pupils " \
                            "Where passport = ?", \
                            (self.passport,), \
                            "Error in erase")

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
        self.gender = special_read(["M", "F"])

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


def clear(cursor, files):
    for i in files:
        query_from_file(cursor, i, "DROP")

def select_commands(cursor, files):
    for i in files:
        query_from_file(cursor, i, "SELECT")

def create(cursor, files):
    for i in files:
        query_from_file(cursor, i, "CREAT")

def filling(cursor, files):
    for i in files:
        query_from_file(cursor, i, "INSERT")

def getColumns(cursor, table_name, colum_names, limits=[]):
    size = len(colum_names)
    query_str = "SELECT DISTINCT " +\
                "{}, " * (len(colum_names) - 1) + "{} " +\
                "FROM {}\n WHERE 1\n"

    colum_names.append(table_name)
    query_str = query_str.format(*colum_names)
    params = []

    for i in limits:
        query_str += "AND {} = ?\n".format(i[0])
        params.append(i[1])

    query_table(cursor, query_str, params, "Ошибка в запросе проецирования(внутренняя ошибка)")
    return cursor.fetchall()
