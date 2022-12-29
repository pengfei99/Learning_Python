# people.py

from datetime import datetime
from flask import abort, make_response

from learning_python.Lesson11_Python_Web_Flask.RestApiWithSQLAlchemy.src.config import db
from learning_python.Lesson11_Python_Web_Flask.RestApiWithSQLAlchemy.src.models import Person, people_schema, \
    person_schema


# this function will be called when server receives an HTTP request to GET /api/people.
def read_all():
    people = Person.query.all()
    print(people)
    # people_schema which is an instance of the Marshmallow PersonSchema class the was created with the
    # parameter many=True. With this parameter you tell PersonSchema to expect an interable to serialize.
    # This is important because the people variable contains a list of database items.
    return people_schema.dump(people)


# the create method receives a person object. This object must contain lname, which must
# not exist in the database already.
def create(person):
    lname = person.get("lname")
    existing_person = Person.query.filter(Person.lname == lname).one_or_none()

    if existing_person is None:
        # deserialize the person object as new_person and add it db.session
        new_person = person_schema.load(person, session=db.session)
        #  Once you commit new_person to the database, your database engine assigns a
        #  new primary key value and a UTC-based timestamp to the object.
        db.session.add(new_person)
        db.session.commit()
        return person_schema.dump(new_person), 201
    else:
        abort(406, f"Person with last name {lname} already exists")


def read_one(lname):
    # .one_or_none() method returns one person, or return None if no match is found.
    person = Person.query.filter(Person.lname == lname).one_or_none()
    # If a person is found, then person contains a Person object and you return the serialized object.
    # Otherwise, you call abort() with an error.
    if person is not None:
        return person_schema.dump(person)
    else:
        abort(404, f"Person with last name {lname} not found")


def update(lname, person):
    existing_person = Person.query.filter(Person.lname == lname).one_or_none()

    if existing_person:
        update_person = person_schema.load(person, session=db.session)
        existing_person.fname = update_person.fname
        db.session.merge(existing_person)
        db.session.commit()
        return person_schema.dump(existing_person), 201
    else:
        abort(404, f"Person with last name {lname} not found")


def delete(lname):
    existing_person = Person.query.filter(Person.lname == lname).one_or_none()

    if existing_person:
        db.session.delete(existing_person)
        db.session.commit()
        return make_response(f"{lname} successfully deleted", 200)
    else:
        abort(404, f"Person with last name {lname} not found")
