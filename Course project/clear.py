import bd_commands as bcom
database = "database.db"


conn = bcom.create_connection(database)
curr = conn.cursor()
bcom.query_from_file(curr, "clear.sql", "DROP")
conn.commit()
conn.close()