import sqlite3

def create_connection(db_file):
    conn = sqlite3.connect(db_file)
    return conn


def query_table(conn, query_table_sql):
    c = conn.cursor()
    c.execute(query_table_sql)
    for x in c:
        print(x[1])


def query_from_file(conn, file_name, commands_type):
    with open(file_name) as file_query:
        s = file_query.read()
        for c in s.split(commands_type):
            if c == "":
                continue
            c = commands_type + c
            query_table(conn, c)