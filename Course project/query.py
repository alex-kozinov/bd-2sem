import bd_commands as bcom
database = "database.db"


conn = bcom.create_connection(database)
bcom.query_from_file(conn, "query.sql", "SELECT")
conn.commit()
conn.close()
