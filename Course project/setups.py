from bd_commands import *

def changeName(cursor, person):
    print('Ваше текущее Имя: "{} - Вы точно хотите его изменить??(y/n)"'.format(person.name))
    c = input()
    while not (c in ["y", "n"]):
        c = input()

    if c == "n":
        return
    person.read_name()
    person.erase(cursor)
    person.insert(cursor)

def changeSurname(cursor, person):
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

def changeMidname(cursor, person):
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

def changeCity(cursor, person):
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

def changeGender(cursor, person):
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

def printOlympiadsResults(cursor, person):
    query_table(cursor, \
    """
    SELECT Olympiads.name, Olympiads.subject, Olympiads.level, Olymp_result.degree
    FROM Olump_result
    INNER JOIN Olympiads
    ON Olump_result.code = Olympiads.code
    WHERE Olymp_result.passport = ?
    """, person.passport, "Ошибка при получении результатов олимпиад")

    cls()
    result = cursor.fetchall()
    if len(result) == 0:
        print("К сожалению, у вас еще нет добавленных результатов олимпиад")
        return
    print_table(("Название Олимпиады", "Предмет", "Уровень", "Степень"), cursor.fetchall())
    input("Введите любую клавишу для продолжения...")
