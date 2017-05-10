from dimka import *
from setups import *


def mainPoint(cursor, person):
    cls()
    print ("\tВведите 0 для выхода c профиля {} {}\n".format(person.name, person.surname),
           "\tВведите 1 для изменения профиля\n",
           "\tВведите 2 для перехода к выполнению комант\n"
           "\tВведите 3 для управления поданными документами\n",
           )
    in_ = input(">")

    if in_ == "0":
        return

    if in_ == "1":
        pointNast(cursor, person)

    if in_ == "2":
        pointCom(cursor, person)

    mainPoint(cursor, person)


def pointCom(cursor, person):
    cls()
    print ("\tВведите 0 для выхода в главное меню\n"
           "\tВведите 1 чтобы получит все факультеты в городе\n",
           "\tВведите 2 ")
    in_ = input(">")

    if in_ == "0":
        return

    if in_ == "1":
        townPoint(cursor)

    pointCom(cursor, person)

