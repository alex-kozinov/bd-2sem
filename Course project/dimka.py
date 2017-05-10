from bd_commands import *

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


