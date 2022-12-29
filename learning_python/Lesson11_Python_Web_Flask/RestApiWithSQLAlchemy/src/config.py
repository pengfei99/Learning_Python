# config.py

import pathlib
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# creates the variable basedir pointing to the directory that the program is running in.
basedir = pathlib.Path(__file__).parent.resolve()

# db_path
db_path=f"sqlite:///{basedir.parent.parent.parent.parent / 'data' / 'people.db'}"
print(db_path)

# uses the basedir variable to create the Connexion app instance and give it the path to the directory
# that contains your specification file.
connex_app = connexion.App(__name__, specification_dir=basedir)
# creates a variable, app, which is the Flask instance initialized by Connexion.
app = connex_app.app
#  tell SQLAlchemy to use SQLite as the database and a file named people.db as the database file
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{basedir.parent.parent.parent.parent / 'data' / 'people.db'}"
#  turns the SQLAlchemy event system off. The event system generates events that are useful in event-driven programs,
#  but it adds significant overhead. Since you’re not creating an event-driven program, you turn this feature off.
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# initializes SQLAlchemy by passing the app configuration information to SQLAlchemy and
# assigning the result to a db variable.
db = SQLAlchemy(app)
# initializes Marshmallow and allows it to work with the SQLAlchemy components attached to the app.
ma = Marshmallow(app)