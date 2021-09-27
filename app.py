from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return '<h1>Hello World :)</h1>'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return "Hello {0}".format(name)

@app.route('/f/<degree>')
def greet(degree=0):
    return "Hello {0}".format(degree)


if __name__ == '__main__':
    app.run()
