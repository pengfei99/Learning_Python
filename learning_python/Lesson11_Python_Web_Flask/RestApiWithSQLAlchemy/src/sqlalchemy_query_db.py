import pathlib

from sqlalchemy import create_engine

from learning_python.Lesson11_Python_Web_Flask.RestApiWithSQLAlchemy.src.models import Person

db_url=f"sqlite:///{pathlib.Path(__file__).parent.resolve().parent.parent.parent.parent / 'data' / 'people.db'}"

engine = create_engine(db_url, echo = True)
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind = engine)
session = Session()
result = session.query(Person).all()

for row in result:
    print("Id: ", row.id, ", LName: ", row.lname)