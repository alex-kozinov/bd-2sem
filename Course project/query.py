import bd_commands as bcom
database = "database.db"


conn = bcom.create_connection(database)
curr = conn.cursor()
bcom.query_from_file(curr, "query.sql", "SELECT")
conn.commit()
conn.close()
