# Python REST APIs With Flask, and SQLAlchemy for persistence

In this project, how to create a REST API with Flask and interact with it using CRUD operations. If you want to 
refresh your knowledge on working with APIs, read this [document](https://realpython.com/api-integration-in-python/). 
We will use **Flask** as the microservice framework, and **connexion** to handle OpenAPI HTTP requests
For more information about connexion, please visit this [site](https://connexion.readthedocs.io/en/latest/). 
Finally, we will use SQLAlchemy as our ORM to realize the CRUD operations on a DB.

This REST API is design to keep track of notes for people that may visit you throughout the year. In this tutorial, 
you’ll create people like the _Tooth Fairy, the Easter Bunny, and Knecht Ruprecht_.


## Planning the API

Besides building the Flask project foundation, you’re going to create a REST API that provides access to a collection 
of people and to the individuals within that collection. Here’s the API design for the people collection:


| Action	 | HTTP Verb	 | URL Path	            | Description                  |
|---------|------------|----------------------|------------------------------|
| Read	   | GET	       | /api/people	         | Read a collection of people. |
| Create	 | POST	      | /api/people	         | Create a new person.         |
| Read	   | GET	       | /api/people/<lname>	 | Read a particular person.    |
| Update	 | PUT	       | /api/people/<lname>	 | Update an existing person.   |
| Delete	 | DELETE	    | /api/people/<lname>	 | Delete an existing person.   |

The REST API that you’ll be building will serve a simple people data structure where the people are keyed to the last name, and any updates are marked with a new timestamp.

The dataset that you’ll be working with looks like this:

```python
PEOPLE = {
    "Fairy": {
        "fname": "Tooth",
        "lname": "Fairy",
        "timestamp": "2022-10-08 09:15:10",
    },
    "Ruprecht": {
        "fname": "Knecht",
        "lname": "Ruprecht",
        "timestamp": "2022-10-08 09:15:13",
    },
    "Bunny": {
        "fname": "Easter",
        "lname": "Bunny",
        "timestamp": "2022-10-08 09:15:27",
    }
}
```
One of the purposes of an API is to decouple the data from the application that uses it, thereby hiding 
the data implementation details. Later in this tutorial series, you’ll save your data in a database. But for 
the start, an in-memory data structure works fine.

## Initiate Flask Project

Add dependencies

```shell
pip install Flask connexion[swagger-ui]
```

Creat an entry point `src/app.py` file. The html templates such as home.html are located at `/templates`

The project structure should look like this:
```text
src/
│
├── templates/
│   └── home.html
│
└── app.py
```

Now, if you run the 
