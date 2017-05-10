from dimka import *
from setups import *


def mainPoint(cursor, person):
    while True:
        cls()
        print ("\tВведите 0 для выхода c профиля {} {}\n".format(person.name, person.surname),
               "\tВведите 1 для изменения профиля\n",
               "\tВведите 2 для перехода к выполнению комант\n"
               "\tВведите 3 для управления подаными документами\n",
               )
        in_ = input(">")
    
        if in_ == "0":
            return
    
        if in_ == "1":
            pointNast(cursor, person)

        if in_ == "2":
            pointCom(cursor, person)


def pointCom(cursor, person):
    while True:
        cls()
        print ("\tВведите 0 для выхода в главное меню\n"
               "\tВведите 1 чтобы получить все университеты в городе\n",
               "\tВведите 2 чтобы получить все факультеты в университете")
        in_ = input(">")

        if in_ == "0":
            return

        if in_ == "1":
            pointUniverInTown(cursor)
        if in_ == "2":
            pointFakultInUniversity(cursor)

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
