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
def to_fahrenheit(degree=""):
    try:
        return_value = "{0}".format(float(degree) * 9.0 / 5 + 32)
    except ValueError:
        return_value = ""
    return return_value


@app.route('/c/<degree>')
def to_celsius(degree=""):
    try:
        return_value = "{0}".format(5 / 9 * (float(degree) - 32))
    except ValueError:
        return_value = ""
    return return_value


if __name__ == '__main__':
    app.run()
