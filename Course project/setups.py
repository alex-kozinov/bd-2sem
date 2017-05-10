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

def deleteDocsFromFaculty(cursor, person):
    while True:
        print("\tВведите 0 для выхода в предыдущее меню\n" \
              "\tВведите 1, если хотите подать документы\n")

        in_ = input(">")

        if in_ == "0":
            return

        if in_ == "1":
            code = -1
            cls()
            print("Введите код факультета, из которова вы хотите забрать документы (или q для отмены)")
            while True:

                in_ = input(">")

                if in_ == "q":
                    break

                code = input(">")
                faculty_codes = getColumns(cursor, "Documents",
                                                   ["faculty_code", ],
                                                   [("passport", person.passport)]
                                           )
                if not (code in faculty_codes):
                    print("Вы не подавали документы в этот вуз")
                    code = -1
                    continue

                code = int(code)

            if code == -1:
                continue

            query_table(cursor, "DELETE FROM Documents\nWHERE faculty_code = ?", code,
                        "Ошибка в удалении поданного документа")
            
