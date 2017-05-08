from bd_commands import *

def fakultInTown(cursor, nameTown) 
	table = query_table(cursor, "SELECT Name FROM Faculty WHERE City == ?", (nameTown), "Dimka fail!")
	print table

