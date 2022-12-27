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

Creat an entry point `src/app.py` file and add below content. 
```python
# app.py

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
```

The html templates such as home.html are located at `/templates`

The project structure should look like this:
```text
src/
│
├── templates/
│   └── home.html
│
└── app.py
```

Now, if you run the below command, a web server will be running and listens to port 8000.

## Adding the first endpoint

To add the endpoint, we will use `Connexion` package, which we installed in the previous section.

`The Connexion module allows a Python program to use the OpenAPI specification with Swagger.` The OpenAPI 
Specification is an API description format for REST APIs and provides a lot of functionality, including:
- Validation of input and output data to and from your API
- Configuration of the API URL endpoints and the expected parameters

When you use OpenAPI with Swagger, you can create a user interface (UI) to explore the API. All of this can happen 
when you create a configuration file that your Flask application can access.

### Create the API Configuration File

The Swagger configuration file is a `YAML or JSON` file containing your OpenAPI definitions. This file contains 
all of the information necessary to configure your server to provide input parameter validation, output response 
data validation, and URL endpoint definition.

Create a file named **swagger.yml** and add below content to it

```yaml
# swagger.yml

# specify which version of openapi you use
#  just like each new Python version includes new features, there may be keywords added or 
#  deprecated in the OpenAPI specification.
openapi: 3.0.0

# set up basic info of your api
info:
  title: "RP Flask REST API" #  Title included in the Connexion-generated UI system
  description: "An API about people and notes" # Description of what the API provides or is about
  version: "1.0.0" # Version value for the API

# By providing "/api" as the value of url, you’ll be able to access all of your API paths relative
#  to http://localhost:8000/api.
servers:
  - url: "/api"

# define your API endpoints in a paths block:
# Below config creates the GET /api/people URL endpoint that you can access at http://localhost:8000/api/people.
paths:
  /people: # The relative URL of your API endpoint
    get: # The HTTP method that this URL endpoint will respond to
      operationId: "people.read_all" # The Python function that’ll respond to the request
      tags: # The tags assigned to this endpoint, which allow you to group the operations in the UI
        - "People"
      summary: "Read the list of people" # The UI display text for this endpoint
      responses: # The status codes that the endpoint responds with
        "200":
          description: "Successfully read people list"
```

> operationId must contain a `string`. Connexion will use "people.read_all" to find a Python function named 
  read_all() in a people module of your project. You’ll create the corresponding Python code later in this 
  tutorial.


The **swagger.yml** file is like a blueprint for your API. With the specifications that you include in swagger.yml, 
you define what data your web server can expect and how your server should respond to requests. But so far, your 
Flask project doesn’t know about your swagger.yml file. Read on to use Connexion to connect your OpenAPI 
specification with your Flask app.

## Add Connexion to the App

There are two steps to adding a REST API URL endpoint to your Flask application with Connexion:

1. Add an API configuration file to your project.
2. Connect your Flask app with the configuration file.

We have done step1, now let's do step2. Update your app.py with below content

```python
# app.py

from flask import render_template # Remove: import Flask
import connexion

app = connexion.App(__name__, specification_dir="./")
app.add_api("swagger.yml")

@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
```

## Implement the logic of your endpoint


In the swagger.yml file, you configured Connexion with the operationId value "people.read_all". So, when the 
API gets an HTTP request for GET /api/people, your Flask app calls a read_all() function within a people module.

To make this work, create a people.py file with a read_all() function:

```python
# people.py

from datetime import datetime

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

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

def read_all():
    return list(PEOPLE.values())
```

After adding above code, restart your server. and type the url : `http://localhost:8000/api/people`

The server will generate an API Documentation: `http://localhost:8000/api/ui`

## Complete the rest of the api

### Work with Components

Before we define new API paths(endpoint) in swagger.yml, we will add a new block for `components`. Components are
building blocks in your OpenAPI specification that you can reference from other parts of your specification.

```yaml
servers:
  - url: "/api"

components:
  schemas:
    Person: # define the schema of Person
      type: "object" # the data type o the schema
      required: # the required properties, The dash(-) in front indicates that required can contain a list of properties
        - lname
      properties: # Any required property must also exist in properties
        fname:
          type: "string"
        lname:
          type: "string"
```

The type key defines the value associated with its parent key. For Person, all properties are strings. You’ll 
represent this schema in your Python code as a dictionary later in this tutorial.

### Create a new endpoint in path /people

This time, we will use post method to create a new Person

```yaml
paths:
  /people:
    get:
        # ...
    post:
      operationId: "people.create" # the python function that will be called
      tags:
        - People
      summary: "Create a person"
      requestBody:
          description: "Person to create"
          required: True
          content:
            application/json:
              schema:
                x-body-name: "person"
                $ref: "#/components/schemas/Person"
      responses:
        "201": # 201 HTTP status code, which is a success response that indicates the creation of a new resource.
          description: "Successfully created person"
```

The structure for post looks similar to the existing `get schema`. One difference is that you also send `requestBody` 
to the server. After all, you need to tell Flask the information that it needs to create a new person. Another 
difference is operationId, which you set to people.create.

We need to add the creat() method in people.py

```python
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
        abort(
            406,
            f"Person with last name {lname} already exists",
        )
```

###  Handle a Person
So far, you’re able to create a new person and get a list with all your people. In this section, you’ll update 
swagger.yml and people.py to work with a new path that handles a single existing person.

Open swagger.yml and add the code below:

```yaml
components:
  schemas:
    # ...
  parameters:
    lname:
      name: "lname"
      description: "Last name of the person to get"
      in: path
      required: True
      schema:
        type: "string"

paths:
  /people:
    # ...
  /people/{lname}: # create a new path /people/{lname} path
    get:
      operationId: "people.read_one"
      tags:
        - People
      summary: "Read one person"
      parameters:
        - $ref: "#/components/parameters/lname"
      responses:
        "200":
          description: "Successfully read person"
```

The above code allow you to get one people information via its lname. 

We will also add update and delete method to manage one people.

```yaml
put:
      tags:
        - People
      operationId: "people.update"
      summary: "Update a person"
      parameters:
        - $ref: "#/components/parameters/lname"
      responses:
        "200":
          description: "Successfully updated person"
      requestBody:
        content:
          application/json:
            schema:
              x-body-name: "person"
              $ref: "#/components/schemas/Person"
    
    delete:
      tags:
        - People
      operationId: "people.delete"
      summary: "Delete a person"
      parameters:
        - $ref: "#/components/parameters/lname"
      responses:
        "204":
          description: "Successfully deleted person"
```

We need to add the corresponding logic in the `people` module

```python
def update(lname, person):
    if lname in PEOPLE:
        PEOPLE[lname]["fname"] = person.get("fname", PEOPLE[lname]["fname"])
        PEOPLE[lname]["timestamp"] = get_timestamp()
        return PEOPLE[lname]
    else:
        abort(
            404,
            f"Person with last name {lname} not found"
        )


def delete(lname):
    if lname in PEOPLE:
        del PEOPLE[lname]
        return make_response(
            f"{lname} successfully deleted", 200
        )
    else:
        abort(
            404,
            f"Person with last name {lname} not found"
        )

```

Now, our api is complete, you can test all method and check their doc by using **http://127.0.0.1:8000/api/ui/**