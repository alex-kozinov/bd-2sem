from bd_commands import *

def pointUniverInTown(cursor):
    cls()
    print ("Введите город на русском: ")
    in_ = input(">")
    universityInTown(cursor, in_)

def pointFakultInUniversity(cursor):
    cls()
    print ("Введите город на русском: ")
    inCity = input(">")
    print ("Введите университет на русском: ")
    inUniver = input(">")
    fakultetInUniversity(cursor, inCity, inUniver)

def universityInTown(cursor, nameTown):
    query_table(cursor, "SELECT DISTINCT university FROM Faculty WHERE city=?", (nameTown, ), "Dimka fail!")
    cls()
    print_table(["университет"], cursor.fetchall())
    input("Нажмите клавишу для продолжения...")

def fakultetInUniversity(cursor, nameTown, nameUniversity):
    query_table(cursor, "SELECT DISTINCT name, faculty_code FROM Faculty WHERE university=? AND city=?", 
				(nameUniversity, nameTown), "Dimka fail!")
    cls()
    print_table(["факультет", "код факультета"], cursor.fetchall())
    input("Нажмите клавишу для продолжения...")


