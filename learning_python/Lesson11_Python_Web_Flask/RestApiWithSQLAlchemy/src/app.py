# app.py

from flask import render_template  # Remove: import Flask

import config
from models import Person

# The config module provides the Connexion-flavored Flask app for you. Therefore, you don’t create a new Flask
# app in app.py anymore, but reference config.connex_app
app = config.connex_app
app.add_api(config.basedir / "swagger.yml")


# you connect the URL route "/" to the home() function by decorating it with @app.route("/").
# This function calls the Flask render_template() function to get the home.html file from the templates
# directory and return it to the browser.
@app.route("/")
def home():
    people = Person.query.all()
    return render_template("home.html", people=people)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
