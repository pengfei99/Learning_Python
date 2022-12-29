import sqlite3
import pathlib


def create_db(path: str):
    conn = sqlite3.connect(path)
    columns = [
        "id INTEGER PRIMARY KEY",
        "lname VARCHAR UNIQUE",
        "fname VARCHAR",
        "timestamp DATETIME",
    ]
    create_table_cmd = f"CREATE TABLE person ({','.join(columns)})"
    conn.execute(create_table_cmd)


def get_path():
    current = pathlib.Path.cwd().parent.parent.parent.parent / 'data' / 'people.db'
    return current


def main():
    create_db(str(get_path()))


if __name__ == "__main__":
    main()
