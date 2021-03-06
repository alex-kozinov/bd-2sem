from simple import *
from printInfo import *
from setups import *
from service import *


def mainPoint(cursor, person):
    while True:
        cls()
        print ("\tВведите 0 для выхода c профиля {} {}\n".format(person.name, person.surname),
               "\tВведите 1 для изменения профиля\n",
               "\tВведите 2 для перехода к выполнению команд\n"
               "\tВведите 3 для управления подаными документами\n",)

        in_ = input(">")
    
        if in_ == "0":
            return
    
        if in_ == "1":
            pointSet(cursor, person)

        if in_ == "2":
            pointCom(cursor, person)

        if in_ == "3":
            pointService(cursor, person)


def pointCom(cursor, person):
    while True:
        cls()
        print ("\tВведите 0 для выхода в главное меню\n",
               "\tВведите 1, чтобы получить все ВУЗы в городе\n",
               "\tВведите 2, чтобы получить все факультеты в ВУЗе\n",
               "\tВведите 3, чтобы получить все факультеты, на которые Вы подали документы\n",
               "\tВведите 4, чтобы получить список всех предметов\n",
               "\tВведите 5, чтобы получить список всех олимпиад\n",
               "\tВведите 6, чтобы получить результаты ЕГЭ\n",
               "\tВведите 7, чтобы получить список добавленных олимпиад\n")
        in_ = input(">")

        if in_ == "0":
            return

        if in_ == "1":
            printUniversitiesInCity(cursor)

        if in_ == "2":
            printFacultiesInUniversity(cursor)

        if in_ == "3":
            printFacultiesWithDocs(cursor, person)

        if in_ == "4":
            printSubjects(cursor)

        if in_ == "5":
            printOlympiads(cursor)

        if in_ == "6":
            printExamsResults(cursor, person)
    
        if in_ == "7":
            printOlympiadsResults(cursor, person)



def pointSet(cursor, person):
    while True:
        cls()
        print("\tВведите 0 для выхода в предыдущее меню\n",
              "\tВведите 1 для изменения ФИО\n",
              "\tВведите 2 для изменения пола\n",
              "\tВведите 3 для изменения города\n")

        in_ = input(">")

        if in_ == "0":
            return

        if in_ == "1":
            changeFIO(cursor, person)    
        
        if in_ == "2":
            changeGender(cursor, person)

        if in_ == "3":
            changeCity(cursor, person)
 
def changeFIO(cursor, person):
    while True:
        cls()
        print("\tВведите 0 для выхода в предыдущее меню\n",
              "\tВведите 1 для изменения фамилии\n",
              "\tВведите 2 для изменения имени\n",
              "\tВведите 3 для изменения отчества\n")

        in_ = input(">")

        if in_ == "0":
            return

        if in_ == "1":
            changeSurname(cursor, person)        
       
        if in_ == "2":
            changeName(cursor, person)

        if in_ == "3":
            changeMidname(cursor, person)
    
def pointService(cursor, person):
    while True:
        cls()
        print("\tВведите 0 для выхода в предыдущее меню\n",
              "\tВведите 1 для ввода результатов ЕГЭ\n",
              "\tВведите 2 для ввода результатов олимпиад\n",
              "\tВведите 3 для подачи документов на факультет\n",
              "\tВведите 4, если хотите забрать документы с факультета")
        
        in_ = input(">")
        
        if in_ == "0":
            return
        
        if in_ == "1":
            insertExamsResults(cursor, person)
            
        if in_ == "2":
            insertOlympiadsResults(cursor, person)
            
        if in_ == "3":
            insertDocsOnFaculty(cursor, person)    

        if in_ == "4":
            deleteDocsFromFaculty(cursor, person)
