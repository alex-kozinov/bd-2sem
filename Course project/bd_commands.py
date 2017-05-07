import sqlite3

def create_connection(db_file):
    conn = sqlite3.connect(db_file)
    return conn


def query_table(cursor, query_sql, params, error_text):
    try:
        if params == None:
            cursor.execute(query_sql)
        else:
            cursor.execute(query_sql, params)
    except sqlite3.Error asВ e:
        print(error_text, e.args[0])




def query_from_file(cursor, file_name, commands_type):
    with open(file_name) as file_query:
        s = file_query.read()
        for c in s.split(commands_type):
            if c == "":
                continue
            c = commands_type + c
            query_table(cursor, c, None, "Wrong command format in file")
            for i in cursor:
                print(str(i))


