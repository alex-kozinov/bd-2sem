from bd_commands import *

def printUniversitiesInCity(cursor):
    cls()
    print ("Введите город на русском: ")
    in_ = input(">")
    universityInTown(cursor, in_)

def printFacultiesInUniversity(cursor):
    cls()
    print ("Введите город на русском: ")
    inCity = input(">")
    print ("Введите университет на русском: ")
    inUniver = input(">")
    fakultetInUniversity(cursor, inCity, inUniver)

def printFacultiesWithDocs(cursor, person):
    cls()
    facultiesWithDocs(cursor, person)

def printOlympiads(cursor):
	cls()
	olympiads(cursor)

def printExamsResults(cursor, person):
    cls()
    examsResults(cursor, person)

def printOlympiadsResults(cursor, person)
    cls()
    olympiadsResult(cursor, person)

def printSubject(cursor):
    cls()
    subject(cursor)



def universityInTown(cursor, nameTown):
    query_table(cursor, "SELECT DISTINCT university FROM Faculty WHERE city=?", (nameTown, ), "Dimka fail!")
    cls()
    if cursor.fetchall() == []: 
        print ("В этом городе нет университетов")
    print_table(["университет"], cursor.fetchall())
    input("Нажмите клавишу для продолжения...")

def fakultetInUniversity(cursor, nameTown, nameUniversity):
    query_table(cursor, "SELECT DISTINCT name, faculty_code FROM Faculty WHERE university=? AND city=?", 
				(nameUniversity, nameTown), "Dimka fail!")
    cls()
    if cursor.fetchall() == []:
        print ("В этом университете нет факультетов")
    print_table(["факультет", "код факультета"], cursor.fetchall())
    input("Нажмите клавишу для продолжения...")

def facultiesWithDocs(cursor, person) {
    query_table(cursor, "\
WITH ac AS (SELECT DISTINCT faculty_code FROM Documents WHERE passport=?)\
SELECT DISTINCT ac.faculty_code, Faculty.name FROM ac INNER JOIN Faculty\
ON ac.faculty_code=Faculty.faculty_code", (person.passport))
    cls()
    if cursor.fetchall() == []:
        print ("Вы ещё никуда не подали документы")
    fa = cursor.fetchall()
    for i in range(0, len(fa)):
        fa[i].append("Копия")
        if fa[i][0] == person.faculty_code:
            fa[i][2] = "Оригинал"
    print_table(["код факультета", "факультет", "тип подачи"], fa)
    input("Нажмите клавишу для продолжения...")
}
def olympiads(cursor):
    query_table(cursor, "SELECT code, name, level FROM Olympiads")
    if cursor.fetchall() == []
        print ("У нас нет олимпиад!")
    print_table(["код олимпиады", "полное имя", "уровень"], cursor.fetchall())
    input("Нажмите клавишу для продолжения")

def examsResults(cursor, person):
    query_table(cursor, "\
WITH pe AS (SELECT subject, rating FROM Exams WHERE passport=?)\
SELECT DISTINCT Subject.subject_name, pe.rating FROM pe INNER JOIN Subject\
ON Subject.subject_code=pe.subject"), (person.passport)
    cls()
    if cursor.fetchall() == []
        print ("Экзамены не заполнины")
    print_table(["предмет", "результат"], cursor.fetchall());

def subject(cursor):
    query_table(cursor? "SELECT DISTINCT subject_code, subgect_name FROM Subject")
    cls()
    if cursor.fetchall() == []
        print ("Предметов нет!")
    print_table(["код предмета", "предмет"], cursor.fetchall())

