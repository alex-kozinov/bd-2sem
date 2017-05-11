from bd_commands import *

def printUniversitiesInCity(cursor):
    cls()
    print ("Введите город: ")
    in_ = input(">")
    universityInTown(cursor, in_)

def printFacultiesInUniversity(cursor):
    cls()
    print ("Введите город: ")
    inCity = input(">")
    print ("Введите университет: ")
    inUniver = input(">")
    facultyInUniversity(cursor, inCity, inUniver)

def printFacultiesWithDocs(cursor, person):
    cls()
    facultiesWithDocs(cursor, person)

def printOlympiads(cursor):
	cls()
	olympiads(cursor)

def printExamsResults(cursor, person):
    cls()
    examsResults(cursor, person)

def printOlympiadsResults(cursor, person):
    cls()
    olympiadsResults(cursor, person)

def printSubjects(cursor):
    cls()
    subjects(cursor)

def universityInTown(cursor, nameTown):
    query_table(cursor, 
    """
    SELECT DISTINCT university 
    FROM Faculty WHERE city = ?
    """,  (nameTown,), "Incorrect data: ")
    cls()
    res = cursor.fetchall()
    if res == []: 
        print ("В этом городе нет университетов")
    else:
        print_table(["университет"], res)
    input("Нажмите клавишу для продолжения...")

def facultyInUniversity(cursor, nameTown, nameUniversity):
    query_table(cursor, 
    """
    SELECT DISTINCT name, faculty_code FROM Faculty 
    WHERE university = ? AND city = ?
    """, (nameUniversity, nameTown), "Incorrect data: ")
    cls()
    res = cursor.fetchall()
    if res == []:
        print ("В этом университете нет факультетов")
    else:
        print_table(["факультет", "код факультета"], res)
    input("Нажмите клавишу для продолжения...")

def facultiesWithDocs(cursor, person):
    query_table(cursor, \
    """
    WITH Q AS (SELECT DISTINCT faculty_code FROM Documents WHERE passport = ?) 
    SELECT DISTINCT Q.faculty_code, Faculty.name FROM Q INNER JOIN Faculty 
    ON Q.faculty_code = Faculty.faculty_code
    """, (person.passport,), "Incorrect data")
    cls()
    res = cursor.fetchall()
    if res == []:
        print ("Вы ещё никуда не подали документы")
    else:
        for i in range(0, len(res)):

            if (person.faculty_code != "NULL" and 
                    res[i][0] == int(person.faculty_code)):
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
                s += getColumns(cursor, "Exams", ["rating"], \
                                        [("passport", competitors[k][0]), \
                                        ("subject", int(subject))])[0][0]
            summary.append((s, competitors[k][0]))
            if competitors[k][0] == person.passport:
                our_s = s
    
        place = 1

        for (s, ps) in summary:
            if s > our_s:
                place += 1

        res[i] = (*res[i], place)
        print(res[i])

    print_table(["код факультета", "факультет", "копия/оригинал", "место"], res)
    input("Нажмите клавишу для продолжения...")

def olympiads(cursor):
    query_table(cursor, 
    """
    SELECT code, name, level FROM Olympiads
    """, None, "Incorrect data")
    res = cursor.fetchall()
    if res == []:
        print ("У нас нет олимпиад!")
    else:
        print_table(["код олимпиады", "полное имя", "уровень"], res)
    input("Нажмите клавишу для продолжения...")

def examsResults(cursor, person):
    query_table(cursor, 
    """
    WITH pe AS (SELECT subject, rating FROM Exams WHERE passport = ?) 
    SELECT DISTINCT Subjects.subject_name, pe.rating
    FROM pe 
    INNER JOIN Subjects ON Subjects.subject_code = pe.subject
    """, (person.passport,), "Incorrect data")
    cls()

    res = cursor.fetchall()
    if res == []:
        print ("Нет результатов экзаменов")
    else:
        print_table(["предмет", "результат"], res);
    input("Нажмите клавишу для продолжения...")

def subjects(cursor):
    
    query_table(cursor, 
    """
    SELECT DISTINCT subject_code, subject_name 
    FROM Subjects
    """, None, "Incorrect data")
    cls()
    res = cursor.fetchall()
    if res == []:
        print ("Предметов нет!")
    else:
        print_table(["код предмета", "предмет"], res)
    input("Нажмите клавишу для продолжения...")

def olympiadsResults(cursor, person):
    query_table(cursor, \
    """
    SELECT Olympiads.name, Subjects.subject_name, Olympiads.level, Olymp_result.degree
    FROM Olymp_result
    INNER JOIN Olympiads
    ON Olymp_result.code = Olympiads.code
    INNER JOIN Subjects ON Olympiads.subject = Subjects.subject_code
    WHERE Olymp_result.passport = ?
    """, (person.passport,), "Ошибка при получении результатов олимпиад")

    cls()
    result = cursor.fetchall()
    if len(result) == 0:
        print("К сожалению, у вас еще нет добавленных результатов олимпиад")
    else:
        print_table(("Название Олимпиады", "Предмет", "Уровень", "Степень"), result)
    input("Введите любую клавишу для продолжения...")
