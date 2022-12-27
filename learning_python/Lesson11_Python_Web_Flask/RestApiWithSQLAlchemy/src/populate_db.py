import pathlib
import sqlite3


def populate_db(path: str):
    conn = sqlite3.connect(path)
    people = [
        "1, 'Fairy', 'Tooth', '2022-10-08 09:15:10'",
        "2, 'Ruprecht', 'Knecht', '2022-10-08 09:15:13'",
        "3, 'Bunny', 'Easter', '2022-10-08 09:15:27'",
    ]
    for person_data in people:
        insert_cmd = f"INSERT INTO person VALUES ({person_data})"
        conn.execute(insert_cmd)

    conn.commit()


def get_path():
    current = pathlib.Path.cwd().parent.parent.parent.parent / 'data' / 'people.db'
    return current


def main():
    populate_db(str(get_path()))


if __name__ == "__main__":
    main()
