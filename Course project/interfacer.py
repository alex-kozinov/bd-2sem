from dimka import *
database = "database.db"


def print_table(column_name, cort):
    n = len(column_name)
    lens = []

    for x in column_name:
        lens.append(len(column_name))

    for i in range(0, n):
        for j in cort:
            lens[i] = max(lens[i], len(j[i]))

    width = sum(lens[i] for i in range(0, n)) + n + 1
    format_str = "|"
    horisont_str = "+" + "-" * (width - 2) + "+"
    for i in range(0, n):
        number_format = "{0[" + str(i) + "]:>" + str(lens[i]) + "}|"
        format_str = format_str + number_format

    print(horisont_str)
    print(format_str.format(column_name));
    print(horisont_str)
    for i in cort:
        print(format_str.format(i))
        print(horisont_str)

def login(cursor):
    new_pupil = Pupil()
    cls()
    print("\tДобро пожаловать!\n Для идентификации, введите свои номер и серию паспорта.")
    new_pupil.read_passport()

    if not new_pupil.init_with_passport(cursor):
        print("Увы, но ваших данных нет в нашей базе. Введем их сейчас.")
        cls()
        new_pupil.read_other_data()
        new_pupil.insert(cursor)
    return new_pupil

def main():
    conn = create_connection(database)
    while True:
        cursor = conn.cursor()
        person = login(cursor)
        conn.commit()
        print("Поздравляем, {}, вы залогинились".format(person.name))
        print_table((1, 2), (("a", "ab"), ("cad", "a")))
        print("Нажмити y, чтобы продолжить, иначе n")
        answer = input()
        if answer != "y":
            break

    conn.close()

main()