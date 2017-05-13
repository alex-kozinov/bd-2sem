from points import *
database = "database.db"


def login(cursor):
    new_pupil = Pupil()
    cls()
    print_middle("Добро пожаловать!")
    print_middle("Для идентификации, введите свои номер и серию паспорта.")
    new_pupil.read_passport()

    if not new_pupil.init_with_passport(cursor):
        cls()
        print_middle("Увы, но ваших данных нет в нашей базе. Введем их сейчас.")
        new_pupil.read_other_data()
        new_pupil.insert(cursor)
    return new_pupil

def main():
    conn = create_connection(database)
    cursor = conn.cursor()
    person = login(cursor)
    cls()
    print_middle("Поздравляем, {}, вы залогинились".format(person.name))
    end_command()
    conn.commit()
    mainPoint(cursor, person)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()
