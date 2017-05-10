import bd_commands as bcom
database = "database.db"

files = ["filling.sql", "rand_faculty.sql"]

conn = bcom.create_connection(database)
curr = conn.cursor()
for i in files:
    bcom.query_from_file(curr, i, "INSERT")
conn.commit()
conn.close()