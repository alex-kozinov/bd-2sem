from bd_commands import *
import os
database = "database.db"


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


def init_with_passport(cursor, person, passport):
    query_table(cursor, "SELECT * FROM Pupils WHERE passport = " + str(passport),\
                None, "Incorrect passport ")

    res = cursor.fetchall()
    if len(res) == 0:
        return 0

    person.assign_data(res[0])
    return 1


conn = create_connection(database)
while True:
    cursor = conn.cursor()
    person = Pupil()
    cls()
    print("\tДобро пожаловать!\n Для идентификации, введите свои номер и серию паспорта.")
    person.read_passport()
    if not init_with_passport(cursor, person, person.passport):
        print("Увы, но ваших данных нет в нашей базе. Введем их сейчас.")
        cls()
        person.read_other_data()

    person.insert(cursor)
    cls()
    print("Поздравляем, {}, вы залогинились".format(person.name))
    conn.commit()
    print("Нажмити y, чтобы продолжить, иначе n")
    answer = input()
    if answer != "y":
        break
conn.close()


