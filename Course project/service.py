from bd_commands import *

def insertRating(cursor, person):
    cls()
    while True:
        print("\tВведите 0 для выхода в предыдущее меню\n"
              "\tВведите 1, если хотите ввести результаты\n")
        
        in_ = input(">")

        if in_ == "0":
            return

        if in_ == "1":
            cls()
            while True:
                subject = input("Введите название предмета: ")
                if subject not in getColumn("Subjects", "subject_name"):
                    print("Неизвестный предмет\n")
                    continue
                else:
                    break

            while True:
                rating = input("Введите баллы: ")
                rating = int(rating)
                if rating < 0 || rating > 100:
                    print("Некорректные баллы\n")
                    continue
                else:
                    break

            query_table(cursor, "INSERT INTO Exams" \
                                "(passport, subject, rating)" \
                                "VALUES(?, ?, ?)"),
                       (person.passport, subject, rating),
                       "Incorrect data: ")

def insertOlympiadsResults(cursor, person):
    while True:
        
