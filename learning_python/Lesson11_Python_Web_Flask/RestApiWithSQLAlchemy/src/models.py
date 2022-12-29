# models.py

from datetime import datetime
from config import db, ma


# Inheriting from db.Model gives Person the SQLAlchemy features to connect to the database and access its tables.
class Person(db.Model):
    # connects the class definition to the person database table.
    __tablename__ = "person"
    __table_args__ = {'extend_existing': True}
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


# SQLAlchemyAutoSchema tells Marshmallow to look for and then use the internal Meta class.
class PersonSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        # specify which model class this schema will match for
        model = Person
        # With load_instance, you’re able to deserialize JSON data and load Person model instances from it
        load_instance = True
        # get the SQLALchemy session, This is how Marshmallow finds attributes in the Person class and
        # learns the types of those attributes so it knows how to serialize and deserialize them.
        sqla_session = db.session


person_schema = PersonSchema()
people_schema = PersonSchema(many=True)
