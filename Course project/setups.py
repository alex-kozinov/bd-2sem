from bd_commands import *

def changeName(cursor, person):
    cls()
    print_middle('Ваше текущее Имя: "{}". Вы точно хотите его изменить?(y/n)'.format(person.name))
    c = special_read(["y", "n"])
    if c == "n":
        return

    cls()
    person.read_name()
    person.erase(cursor)
    person.insert(cursor)

def changeSurname(cursor, person):
    cls()
    print_middle('Ваша текущая Фамилия: "{}". Вы точно хотите её изменить?(y/n)'.format(person.surname))
    c = c = special_read(["y", "n"])
    if c == "n":
        return

    cls()
    person.read_surname()
    person.erase(cursor)
    person.insert(cursor)

def changeMidname(cursor, person):
    cls()
    print_middle('Ваше текущее Отчество: "{}". Вы точно хотите его изменить?(y/n)'.format(person.midname))
    c = special_read(["y", "n"])
    if c == "n":
        return

    cls()
    person.read_midname()
    person.erase(cursor)
    person.insert(cursor)

def changeCity(cursor, person):
    cls()
    print_middle('Город, который вы указали: "{}". Вы точно хотите его изменить?(y/n)'.format(person.city))
    c = special_read(["y", "n"])
    if c == "n":
        return

    cls()
    person.read_city()
    person.erase(cursor)
    person.insert(cursor)

def changeGender(cursor, person):
    cls()
    gender = "Мужской" if person.gender == "M" else "Женский"
    print_middle('Ваш текущий пол: "{}" - это не наше дело, но вы действительно хотите его изменить?(y/n)'.format(gender))
    c = special_read(["y", "n"])
    if c == "n":
        return

    cls()
    person.read_gender()
    person.erase(cursor)
    person.insert(cursor)
