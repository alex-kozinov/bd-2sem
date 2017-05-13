from bd_commands import *

def printUniversitiesInCity(cursor):
    cls()
    print_middle("Введите название города")

    name_town = read_str()
    res = getColumns(cursor, "Faculty", "university", ["city", name_town])

    cls()
    if res == []:
        print_middle("В этом городе нет университетов")
    else:
        print_table(["университет"], res)

    end_command()

def printFacultiesInUniversity(cursor):
    cls()
    print_middle("Введите город: ")
    name_town = read_str()
    cls()
    print_middle("Введите университет: ")
    name_university = read_str()

    res = getColumns(cursor, "Faculty", ["name, faculty_code"],
                     [("university", name_university), ("city", name_town)])

    cls()
    if res == []:
        print_middle("В этом университете нет факультетов")
    else:
        print_table(["факультет", "код факультета"], res)

    end_command()


def printFacultiesWithDocs(cursor, person):
    query_table(cursor,"""
                WITH Q AS (SELECT DISTINCT faculty_code 
                           FROM Documents 
                           WHERE passport = ?) 
                SELECT DISTINCT Q.faculty_code, Faculty.name 
                FROM Q INNER JOIN Faculty 
                ON Q.faculty_code = Faculty.faculty_code
                """, (person.passport,), "Incorrect data")
    res = cursor.fetchall()

    cls()
    if res == []:
        print_middle("Вы ещё никуда не подали документы")
        end_command()
        return

    for i in range(0, len(res)):
        if (person.faculty_code != "NULL" and \
                    res[i][0] == person.faculty_code):
            res[i] = (*res[i], "Оригинал")
        else:
            res[i] = (*res[i], "Копия")

    for i in range(len(res)):
        competitors = getColumns(cursor, "Documents", ["passport"], \
                                 [("faculty_code", int(res[i][0]))])

        summary = []
        our_s = 0
        for k in range(len(competitors)):
            s = 0
            for j in range(1, 4):
                subject = getColumns(cursor, "Faculty", \
                                     ["subject" + str(j)])[0][0]
                raiting = getColumns(cursor, "Exams", ["rating"], \
                                [("passport", competitors[k][0]), \
                                 ("subject", int(subject))])
                if len(raiting) > 0:
                    s += raiting[0][0]

            summary.append((s, competitors[k][0]))
            if competitors[k][0] == person.passport:
                our_s = s

        place = 1

        for (s, ps) in summary:
            if s > our_s:
                place += 1

        res[i] = (*res[i], place)

    print_table(["код факультета", "факультет", "копия/оригинал", "место"], res)
    end_command()

def printOlympiads(cursor):
    res = getColumns(cursor, "Olympiads", ["code", "name", "level"])

    cls()
    if res == []:
        print_middle("У нас нет олимпиад!")
    else:
        print_table(["код олимпиады", "полное название", "уровень"], res)

    end_command()


def printExamsResults(cursor, person):
    query_table(cursor,"""
                WITH pe AS (SELECT subject, rating 
                            FROM Exams WHERE passport = ?) 
                SELECT DISTINCT Subjects.subject_name, pe.rating
                FROM pe 
                INNER JOIN Subjects 
                ON Subjects.subject_code = pe.subject
                """, (person.passport,), "Incorrect data")
    res = cursor.fetchall()

    cls()
    if res == []:
        print_middle("Нет результатов экзаменов")
    else:
        print_table(["предмет", "результат"], res)

    end_command()

def printOlympiadsResults(cursor, person):
    query_table(cursor, """
                SELECT Olympiads.name, Subjects.subject_name, Olympiads.level, Olymp_result.degree
                FROM Olymp_result
                INNER JOIN Olympiads
                ON Olymp_result.code = Olympiads.code
                INNER JOIN Subjects ON Olympiads.subject = Subjects.subject_code
                WHERE Olymp_result.passport = ?
                """, (person.passport,), "Ошибка при получении результатов олимпиад")
    result = cursor.fetchall()

    cls()
    if len(result) == 0:
        print_middle("К сожалению, у вас еще нет добавленных результатов олимпиад")
    else:
        print_table(("Название Олимпиады", "Предмет", "Уровень", "Степень"), result)

    end_command()


def printSubjects(cursor):
    res = getColumns(cursor, "Subjects", ["subject_code", "subject_name"])

    cls()
    if res == []:
        print_middle("Очень странно, но в нашей базе нет предметов:(")
    else:
        print_table(["код предмета", "предмет"], res)

    end_command()
