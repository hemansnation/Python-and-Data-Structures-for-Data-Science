from flask import Flask

app = Flask(__name__)         # '__main__'

@app.route('/')
def index():
    return "Welcome to Flask"


if __name__ == '__main__':
    app.run(port=5000)