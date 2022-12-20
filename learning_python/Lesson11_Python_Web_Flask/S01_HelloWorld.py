# set up env, you only need to do `pip install flask`

from flask import Flask

app = Flask(__name__)


# The route() function of the Flask class is a decorator, which tells the
# application which URL should call the associated function.
# in this example, ‘/’ URL is bound with hello_world() function. Hence,
# when the home page of web server is opened in browser, the output of this
# function will be rendered.
@app.route('/')
def hello_world():
    return 'Hello World'


# the run() method of Flask class runs the application on the local development server.
# it has four optional parameters: app.run(host, port, debug, options)
# host: Hostname to listen on. Defaults to 127.0.0.1 (localhost). Set to ‘0.0.0.0’ to have server
#       available externally
# port: port to listen on. Defaults to 5000
# debug: Defaults to false. If set to true, provides a debug information
# options: To be forwarded to underlying Werkzeug server.
if __name__ == '__main__':
    host = '0.0.0.0'
    port = 8080
    debug = True
    app.run(host, port, debug)
