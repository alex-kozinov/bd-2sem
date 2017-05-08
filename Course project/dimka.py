from bd_commands import *

def mainPoint(cur): 
    cls()
    print ("\tВведите 1 для изменения профиля\n",
           "\tВведите 2 для перехода к выполнению команд")
    in_ = input()
    if in_ == "1":
        pointNast(cur)
    if in_ == "2":
        pointCom(cur)

def pointCom(cur):
    cls()
    print ("\tВведите 1 чтобы получит все факультеты в городе\n",
           "\tВведите 2 ")
    in_ = input();
    if in_ == "1":
        townPoint(cur)

def townPoint(cur): 
    cls()
    print ("Введите город на русском: ")
    in_ = input()
    fakultInTown(cur, in_)

def fakultInTown(cursor, nameTown):
    query_table(cursor, "SELECT name FROM Faculty WHERE city == ?", (nameTown), "Dimka fail!")
    print (cursor.fetchol())
    #print_table(("фальтет"), cursor.fetchol())
