import bd_commands as bcom
database = "database.db"


conn = bcom.create_connection(database)
curr = conn.cursor()
bcom.query_from_file(curr, "create.sql", "CREATE")
conn.commit()
conn.close()