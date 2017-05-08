from dimka import *
database = "database.db"


def init_with_passport(cursor, person, passport):
    query_table(cursor, "SELECT * FROM Pupils WHERE passport = " + str(passport),\
                None, "Incorrect passport ")

    res = cursor.fetchall()
    if len(res) == 0:
        return 0

    person.assign_data(res[0])
    return 1



conn = create_connection(database)
while True:
    cursor = conn.cursor()
    person = Pupil()
    cls()
    print("\tДобро*t()
    if not init_with_passport(cursor, person, person.passport):
        print("Увы, но ваших данных нет в нашей базе. Введем их сейчас.")
        cls()
        person.read_other_data()

    person.insert(cursor)
    cls()
    print("Поздравляем, {}, вы залогинились".format(person.name))
    conn.commit()

    print("Нажмити y, чтобы продолжить, иначе n")
    answer = input()
    if answer != "y":
        break
conn.close()


