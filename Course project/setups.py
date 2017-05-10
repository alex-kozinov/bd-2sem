from bd_commands import *

def insertName(cursor, person):
    print('Ваше текущее Имя: "{} - Вы точно хотите его изменить??(y/n)"'.format(person.name))
    c = input()
    while not (c in ["y", "n"]):
        c = input()

    if c == "n":
        return
    person.read_name()
    person.erase(cursor)
    person.insert(cursor)

def insertSurname(cursor, person):
    print('Ваша текущая Фамилия: "{} - Вы точно хотите её изменить??(y/n)"'.format(person.name))
    c = input()
    while not (c in ["y", "n"]):
        c = input()

    if c == "n":
        return
    cls()
    person.read_surname()
    person.erase(cursor)
    person.insert(cursor)

def insertMidname(cursor, person):
    print('Ваше текущее Отчество: "{} - Вы точно хотите его изменить??(y/n)"'.format(person.name))
    c = input()
    while not (c in ["y", "n"]):
        c = input()

    if c == "n":
        return
    cls()
    person.read_midname()
    person.erase(cursor)
    person.insert(cursor)

def insertCity(cursor, person):
    print('Город, который вы указали: "{} - Вы точно хотите его изменить??(y/n)"'.format(person.name))
    c = input()
    while not (c in ["y", "n"]):
        c = input()

    if c == "n":
        return
    cls()
    person.read_city()
    person.erase(cursor)
    person.insert(cursor)

def insertGender(cursor, person):
    gender = "Мужской" if person.gender == "M" else "Женский"
    print('Ваш текущий пол: {} - это не наше дело, но вы действительно хотите его изменить??(y/n)'.format(gender))
    c = input()
    while not (c in ["y", "n"]):
        c = input()

    if c == "n":
        return

    cls()
    person.read_gender()
    person.erase()
    person.insert()

