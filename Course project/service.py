from bd_commands import *

def insertExamsResults(cursor, person):
    cls()
    while True:
        print("\tВведите 0 для выхода в предыдущее меню\n"
              "\tВведите 1, если хотите ввести результаты ЕГЭ\n")
        
        in_ = input(">")

        if in_ == "0":
            return

        if in_ == "1":
            cls()
            
            subject = 0
            
            print("\nВведите код предмета(или q для выхода): ")

            while True:
                subject = input(">")
                if subject == "q":
                    break
                elif not ((int(subject),) in 
                        getColumns(cursor, "Subjects", ["subject_code"])):
                    print("Некорректный код")
                    continue
                elif (person.passport, int(subject)) in \
                        getColumns(cursor, "Exams", ["passport", "subject"]):
                    print("Результаты уже добавлены")
                else:
                    break
            cls()

            if subject == "q":
                continue

            rating = 0

            print("Введите баллы(или q для выхода): ")

            while True:
                rating = input(">")
                if rating == "q":
                    break
                rating = int(rating)
                if int(rating) < 0 or int(rating) > 100:
                    print("Некорректные баллы\n")
                    continue
                else:
                    break

            cls()

            if rating == "q":
                continue

            query_table(cursor, "INSERT INTO Exams " \
                                "(passport, subject, rating) " \
                                "VALUES(?, ?, ?)", \
                       (person.passport, subject, rating), \
                       "Incorrect data: ")

def insertOlympiadsResults(cursor, person):
    cls()
    while True:
        print("\tВведите 0 для выхода в предыдущее меню\n"
              "\tВведите 1, если хотите ввести результаты олимпиад\n")

        in_ = input()

        if in_ == "0":
            return

        if in_ == "1":
            cls()

            code = 0
            
            print("Введите код олимпиады(или q для выхода): ")

            while True:
                code = input(">")
                if code == "q":
                    break
                elif not ((int(code),) in 
                        getColumns(cursor, "Olympiads", ["code"])):
                    print("Некорректный код")
                elif (int(code),) in 
                        getColumns(cursor, "Olymp_result", ["code"]):
                    print("Результаты уже добавлены")
                else:
                    break
            
            cls()

            if code == "q":
                continue

            degree = 0

            print("Введите степень диплома(или q для выхода): ")

            while True:
                degree = input(">")
                if degree == "q":
                    break
                if int(degree) < 0 or int(degree) > 3:
                    print("Некорректная степень")
                else:
                    break

            cls()

            if degree == "q":
                continue

            query_table(cursor, "INSERT INTO Olymp_result " \
                                "(code, passport, degree) " \
                                "VALUES(?, ?, ?) ", \
                                (int(code), person.passport, int(degree)), \
                                "Incorrect data: ")

def insertDocsOnFaculty(cursor, person):
    cls()
    while True:
        print("\tВведите 0 для выхода в предыдущее меню\n" \
              "\tВведите 1, если хотите подать документы\n")

        in_ = input(">")

        if in_ == "0":
            return

        if in_ == "1":
            
            if len(getColumns(cursor, "Documents", ["faculty_code"], \
                    [("passport", person.passport)])) >= 3:
                print("Вы уже подали документы на 3 факультета")
                continue

            code = 0

            print("Введите код факультета(или q для выхода): ")

            while True:
                code = input(">")
                if code == "q":
                    break
                elif not ((int(code),) in 
                        getColumns(cursor, "Faculty", ["Faculty_code"])):
                    print("Некорректный код")
                elif (person.passport, int(code)) in 
                        getColumns(cursor, "Documents", \
                                   ["passport", "faculty_code"]):
                    print("Вы уже подали документы на этот факультет")
                else:
                    break
            
            if code == "q":
                continue
            
            passed = True

            for i in range(1, 4):
                subject = getColumns(cursor, "Faculty", \
                                     ["subject" + str(i)])[0][0]
                if len(getColumns(cursor, "Exams", ["passport"], \
                                  [("passport", person.passport), \
                                  ("subject", int(subject))])) == 0:
                    passed = False

            if not passed:
                print("Вы не сдали все необходимые экзамены")
                continue

            original = "No"

            print("Оригинал или копия Yes/No(или q для выхода): ")

            while True:
                original = input(">")
                if original == "q":
                    break
                elif original == "Yes" and person.faculty_code != "NULL":
                    print("Вы уже подали оригинал")
                elif original == "Yes" or original == "No":
                    break

            cls()
    
            if original == "q":
                continue

            if original == "Yes":
                person.faculty_code = code
                person.erase(cursor)
                person.insert(cursor)

            query_table(cursor, "INSERT INTO Documents " \
                                "(passport, faculty_code) " \
                                "VALUES(?, ?)", \
                                (person.passport, int(code)), \
                                "Incorrect data: ")

def deleteDocsFromFaculty(cursor, person):
    while True:
        print("\tВведите 0 для выхода в предыдущее меню\n" \
              "\tВведите 1, если хотите забрать документы\n")

        in_ = input(">")

        if in_ == "0":
            return

        if in_ == "1":
            code = -1
            cls()
            print("""
            Введите код факультета, из которого вы хотите забрать документы(или q для выхода): 
            """)
            while True:

                code = input(">")

                if code == "q":
                    break

                faculty_codes = getColumns(cursor, "Documents", \
                                           ["faculty_code"], \
                                           [("passport", person.passport)])
                if not ((int(code),) in faculty_codes):
                    print("Вы не подавали документы в этот вуз")
                    continue
                else:
                    break

            if code == "q":
                continue
            
            if person.faculty_code != "NULL" and 
                    int(person.faculty_code) == int(code):
                person.faculty_code = "NULL"
                person.erase(cursor)
                person.insert(cursor)

            query_table(cursor, "DELETE FROM Documents " \
                                "WHERE faculty_code = ?", \
                                (int(code),), \
                                "Ошибка в удалении поданного документа")

            print("Вы успешно забрали документы")
            
