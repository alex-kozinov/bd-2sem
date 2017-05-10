import sys
import bd_commands as bcomm

base_data = "database.db"

def main():
    size = len(sys.argv)
    if size < 2:
        return

    conn = bcomm.create_connection(base_data)
    cursor = conn.cursor()

    files = []
    for i in range(2, size):
        files.append(sys.argv[i])

    if sys.argv[1] == "CREAT":
        bcomm.create(cursor, files)

    if sys.argv[1] == "FILL":
        bcomm.filling(cursor, files)

    if sys.argv[1] == "CLEAR":
        bcomm.clear(cursor, files)

    if sys.argv[1] == "SELECT":
        bcomm.select_commands(cursor, files)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()
