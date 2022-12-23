# Python REST APIs With Flask, and SQLAlchemy for persistence

In this project, how to create a REST API with Flask and interact with it using CRUD operations. If you want to 
refresh your knowledge on working with APIs, read this [document](https://realpython.com/api-integration-in-python/). 
We will use **Flask** as the microservice framework, and **connexion** to handle OpenAPI HTTP requests
For more information about connexion, please visit this [site](https://connexion.readthedocs.io/en/latest/). 
Finally, we will use SQLAlchemy as our ORM to realize the CRUD operations on a DB.

This REST API is design to keep track of notes for people that may visit you throughout the year. In this tutorial, 
you’ll create people like the _Tooth Fairy, the Easter Bunny, and Knecht Ruprecht_.
## Initiate Flask Project

Add dependencies

```shell
pip install Flask connexion[swagger-ui]
```

Creat an entry point `src/app.py` file.
