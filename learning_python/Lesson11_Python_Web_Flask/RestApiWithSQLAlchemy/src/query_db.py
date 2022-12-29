import pathlib
import sqlite3


def query_db(path: str):
    conn = sqlite3.connect(path)
    # creates a cursor from the connection.
    cur = conn.cursor()
    # uses the cursor to execute a SQL query expressed as a string.
    cur.execute("select * from person")
    #  gets all the records returned by the SQL query and assigns them to the people
    people = cur.fetchall()
    for person in people:
        print(person)


def get_path():
    current = pathlib.Path.cwd().parent.parent.parent.parent / 'data' / 'people.db'
    return current


def main():
    query_db(str(get_path()))


if __name__ == "__main__":
    main()
