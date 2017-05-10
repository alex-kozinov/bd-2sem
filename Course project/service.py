from bd_commands import *

def insertRating(cursor, person):
    cls()
    while True:
        print("\tВведите 0 для выхода в предыдущее меню\n"
              "\tВведите 1, если хотите ввести результаты ЕГЭ\n")
        
        in_ = input(">")

        if in_ == "0":
            return

        if in_ == "1":
            cls()
            
            subject = ""

            while True:
                subject = input("Введите название предмета(или q для выхода): ")                if subject == "q":
                    break
                elif not (subject in getColumns(cursor, "Subjects", ["subject_name"])):
                    print("Неизвестный предмет")
                    continue

                elif (person.passport, subject) in getColums(cursor, "Exams", ["passport", "subject"]):
                    print("Результаты уже добавлены")
                else:
                    break
            
            if subject == "q":
                continue

            rating = 0

            while True:
                rating = input("Введите баллы(или q для выхода): ")
                if rating == "q":
                    break
                rating = int(rating)
                if rating < 0 or rating > 100:
                    print("Некорректные баллы\n")
                    continue
                else:
                    break

            if rating == "q":
                continue

            query_table(cursor, "INSERT INTO Exams" \
                                "(passport, subject, rating)" \
                                "VALUES(?, ?, ?)"),
                       (person.passport, subject, rating),
                       "Incorrect data: ")

def insertOlympiadsResults(cursor, person):
    cls()
    while True:
        print("\tВведите 0 для выхода в предыдущее меню\n"
              "\tВведите 1, если хотите ввести результаты олимпиад\n")

        in_ = input()

        if in_ == "0"
            return

        if in_ == "1":
            cls()

            code = 0

            while True:
                code = input("Введите код олимпиады(или q для выхода): ")
                if code == "q":
                    break
                elif not (code in getColumns(cursor, "Olympiads", ["code"])):
                    print("Некорректный код")
                else:
                    break
            
            if code == "q":
                continue

            subject = ""

            while True:
                subject = input("Введите название предмета(или q для выхода): ")
                if subject == "q":
                    break
                elif not (subject in getColumns(cursor, "Subjects", "name")):
                    print("Некорректное название")
                elif (code, person.passport) in getColumn(cursor, "Olymp_result", ["code", "passport"])
                    
                else:
                    break
            
            if subject == "q":
                continue

            degree = 0

            while True:
                degree = input("Введите степень диплома(или q для выхода): ")
                if degree == "q"
                    break
                degree = int(degree)
                if degree < 0 or degree > 3:
                    print("Некорректная степень")
                else
                    break

            if degree == "q":
                continue

            query_table(cursor, "INSERT INTO Pupils" \
                                "(code, passport, degree)" \
                                "VALUES(?, ?, ?)" \
                                (code, person.passport, degree),
                                "Incorrect data: ")

def insertDocsOnFaculty(cursor, person):
    while True:
        print("\tВведите 0 для выхода в предыдущее меню\n" \ 
              "\tВведите 1, если хотите подать документы\n")

        in_ = input(">")

        if in_ == "0":
            return

        if in_ == "1":
            
            #if len(getColumn(cursor, "Documents", ["passport"]))

            code = 0

            if code == "q":
                continue

            while True:
                code = input("Введите код факультета(или q для выхода): ")
                if code == "q":
                    break
                elif not (code in getColumn(cursor, "Faculty", ["Faculty_code"])):
                    print("Некорректный код")
                elif (person.passport, code) in getColumn(cursor, "Documents", ["passprt", "faculty_code"])
                    print("Вы уже подали документы на этот факультет")
                else:
                    break
            
            original = "No"

            while True:
                original = input("Оригинал или копия Yes/No(или q для выхода): ")
                if original == "q":
                    break
                elif original == "Yes" and person.faculty_code != "NULL":
                    print("Вы уже подали оригинал")

            if original == "q":
                continue

            if original == "Yes":
                person.faculty_code = code

            query_table(cursor, "INSERT INTO Documents" \
                                "(passport, faculty_code)" \
                                "VALUES(?, ?)",
                                (self.passport, code),
                                "Incorrect data: ")
