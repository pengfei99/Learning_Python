# people.py

from datetime import datetime
from flask import abort


# helper function to get current time
def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# add sample data
PEOPLE = {
    "Fairy": {
        "fname": "Tooth",
        "lname": "Fairy",
        "timestamp": get_timestamp(),
    },
    "Ruprecht": {
        "fname": "Knecht",
        "lname": "Ruprecht",
        "timestamp": get_timestamp(),
    },
    "Bunny": {
        "fname": "Easter",
        "lname": "Bunny",
        "timestamp": get_timestamp(),
    }
}


# this function will be called when server receives an HTTP request to GET /api/people.
def read_all():
    return list(PEOPLE.values())


def create(person):
    lname = person.get("lname")
    fname = person.get("fname", "")

    if lname and lname not in PEOPLE:
        PEOPLE[lname] = {
            "lname": lname,
            "fname": fname,
            "timestamp": get_timestamp(),
        }
        return PEOPLE[lname], 201
    else:
        #  abort() helps you send an error message in line 20. You raise the error response when the request body
        #  doesn’t contain a last name or when a person with this last name already exists.
        abort(
            406,
            f"Person with last name {lname} already exists",
        )

def read_one(lname):
    if lname in PEOPLE:
        return PEOPLE[lname]
    else:
        abort(
            404, f"Person with last name {lname} not found"
        )
