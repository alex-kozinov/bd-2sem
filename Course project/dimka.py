from bd_commands import *


def townPoint(cursor):
    cls()
    print ("Введите город на русском: ")
    in_ = input(">")
    fakultInTown(cursor, in_)


def fakultInTown(cursor, nameTown):
    query_table(cursor, "SELECT name FROM Faculty WHERE city=?", (nameTown, ), "Dimka fail!")
    cls()
    print_table(["факультет"], cursor.fetchall())
    input("Нажмите клавишу для продолжения...")