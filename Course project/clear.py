import bd_commands as bcom
database = "database.db"


conn = bcom.create_connection(database)
bcom.query_from_file(conn, "clear.sql", "DROP")
conn.commit()
conn.close()