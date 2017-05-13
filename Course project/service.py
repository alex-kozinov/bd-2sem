from bd_commands import *

def insertExamsResults(cursor, person):
    cls()
    print_middle("Введите код предмета по которому хотите добавить результат или q для выхода.")

    while True:
        subject = input(">")
        if subject == "q":
            break

        if (int(subject),) not in \
                      getColumns(cursor, "Subjects", ["subject_code"]):
            print("Некорректный код")
            continue

        if (person.passport, int(subject)) in \
                getColumns(cursor, "Exams", ["passport", "subject"]):
            print("Результаты уже добавлены")
            continue
        break

    if subject == "q":
        return

    cls()
    print_middle("А теперь введите свои баллы по этому предмету(или q для выхода).")
    rating = 0

    while True:
        rating = input(">")
        if rating == "q":
            break

        if int(rating) not in range(0, 101):
            print("Некорректные баллы\n")
            continue

        break

    if rating == "q":
        return

    query_table(cursor, """
    INSERT INTO Exams (passport, subject, rating) VALUES(?, ?, ?)
    """, (person.passport, subject, rating), "Incorrect data: insert Exams ")

    cls()
    print_middle("Ваши результаты успешно добавлены")
    end_command()


def insertOlympiadsResults(cursor, person):
    cls()
    print_middle("Введите код олимпиады по которой хотите добавить результат или q для выхода")

    code = 0
    while True:
        code = input(">")
        if code == "q":
            break

        if (int(code),) not in \
                    getColumns(cursor, "Olympiads", ["code"]):
            print("Некорректный код")

        if (int(code),) in \
                    getColumns(cursor, "Olymp_result", ["code"]):
            print("Результаты уже добавлены")

        break

    if code == "q":
        return

    cls()
    print_middle("Введите степень диплома(или q для выхода): ")

    degree = 0
    while True:
        degree = input(">")
        if degree == "q":
            break

        if int(degree) not in range(0, 4):
            print("Некорректная степень")
        else:
            break

    cls()

    if degree == "q":
        return

    query_table(cursor, """
    INSERT INTO Olymp_result (code, passport, degree) VALUES(?, ?, ?)
    """, (int(code), person.passport, int(degree)), "Incorrect data: insert olympiads")

    cls()
    print_middle("Ваши результаты успешно добавлены")
    end_command()
    input()


def insertDocsOnFaculty(cursor, person):
    cls()
    if len(getColumns(cursor, "Documents", ["faculty_code"], [("passport", person.passport)])) >= 3:
        print_middle("Вы уже подали документы на 3 факультета")
        end_command()
        return

    print_middle("Введите код факультета, куда хотите подать документы или q для выхода")

    code = 0
    while True:
        code = input(">")
        if code == "q":
            break

        if (int(code),) not in \
                      getColumns(cursor, "Faculty", ["Faculty_code"]):
            print("Некорректный код")
            continue

        if (person.passport, int(code)) in \
            getColumns(cursor, "Documents", ["passport", "faculty_code"]):
            print("Вы уже подали документы на этот факультет")
            continue

        break

    if code == "q":
        return

    passed = True
    for i in range(1, 4):
        subject = getColumns(cursor, "Faculty",["subject" + str(i)],
                             [("faculty_code", int(code))])[0][0]
        if len(getColumns(cursor, "Exams", ["passport"], \
                          [("passport", person.passport), \
                           ("subject", int(subject))])) == 0:
            passed = False

    cls()
    if not passed:
        print_middle("Вы не сдали все необходимые экзамены")
        end_command()
        return

    print_middle("Оригинал или копия Yes/No(или q для выхода): ")

    original = "No"
    while True:
        original = input(">")

        if original == "q":
            break

        if original == "Yes" and person.faculty_code != "NULL":
            print(person.faculty_code)
            print("Вы уже подали оригинал")
            continue

        if original == "Yes" or original == "No":
            break

    if original == "q":
        return

    if original == "Yes":
        person.faculty_code = code
        person.erase(cursor)
        person.insert(cursor)

    query_table(cursor, """
    INSERT INTO Documents (passport, faculty_code) VALUES(?, ?)
    """, (person.passport, int(code)), "Incorrect data: insert docs to faculty")

    cls()
    print_middle("Вы успешно подали {} на факультет №{}".format("оригинал" if original == "Yes" else "копию",
                                                        person.faculty_code))

    end_command()

def deleteDocsFromFaculty(cursor, person):
    cls()
    print_middle("Введите код факультета, из которого вы хотите забрать документы(или q для выхода)")

    code = -1
    faculty_codes = getColumns(cursor, "Documents", \
                               ["faculty_code"], \
                               [("passport", person.passport)])
    while True:
        code = input(">")

        if code == "q":
            break

        if (int(code),) not in faculty_codes:
            print("Вы не подавали документы в этот вуз")
            continue

        break

    if code == "q":
        return

    code = int(code)
    if person.faculty_code == code:
        person.faculty_code = "NULL"
        person.erase(cursor)
        person.insert(cursor)


    query_table(cursor, """
    DELETE FROM Documents
    WHERE faculty_code = ?
    AND passport = ?
    """, (code, person.passport), "Ошибка в удалении поданного документа")

    cls()
    print_middle("Вы успешно забрали документы")
    end_command()
