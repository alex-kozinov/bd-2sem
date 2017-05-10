from bd_commands import *


def townPoint(cursor):
    cls()
    print ("Введите город на русском: ")
    in_ = input(">")
    vuzInTown(cursor, in_)


def vuzInTown(cursor, nameTown):
    query_table(cursor, "SELECT university FROM Faculty WHERE city=?", (nameTown, ), "Dimka fail!")
    cls()
    print_table(["университет"], cursor.fetchall())
    input("Нажмите клавишу для продолжения...")

def universityPoint(cursor):
	cls()
	print ("Введите университет на русском: ")
	in_ = input(">")
	fakultetInUniver(cursor, in_)

def fakultetInUniver(cursor, nameTown):
    query_table(cursor, "SELECT name FROM Faculty WHERE university=?", (nameTown, ), "Dimka fail!")
    cls()
    print_table(["факультет"], cursor.fetchall())
    input("Нажмите клавишу для продолжения...")


