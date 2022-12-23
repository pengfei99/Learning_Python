# app.py

from flask import Flask, render_template

# create a flask app
app = Flask(__name__)


# you connect the URL route "/" to the home() function by decorating it with @app.route("/").
# This function calls the Flask render_template() function to get the home.html file from the templates
# directory and return it to the browser.
@app.route("/")
def home():
    return render_template("home.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
