# models.py

from datetime import datetime
from config import db


# Inheriting from db.Model gives Person the SQLAlchemy features to connect to the database and access its tables.
class Person(db.Model):
    # connects the class definition to the person database table.
    __tablename__ = "person"
    # declares the id column containing an integer acting as the primary key for the table.
    id = db.Column(db.Integer, primary_key=True)
    # defines the last name field with a string value. This field must be unique because you’re using lname
    # as the identifier for a person in a REST API URL.
    lname = db.Column(db.String(32), unique=True)
    # defines the first name field with a string value.
    fname = db.Column(db.String(32))
    # The default=datetime.utcnow parameter defaults the timestamp value to the current utcnow value when a record
    # is created. The onupdate=datetime.utcnow parameter updates the timestamp with the current utcnow value when the
    # record is updated.
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
