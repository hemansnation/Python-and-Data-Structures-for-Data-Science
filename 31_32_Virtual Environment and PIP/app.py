from flask import Flask, render_template

app = Flask(__name__)         # '__main__'

@app.route('/')
def index():
    return "Welcome to Flask"

@app.route('/home')
def home():
    return '<h1>Welcome Home!</h1>'

@app.route('/profile')
def profile():
    goa = "from the goa trip"
    return render_template('index.html', name = goa)


if __name__ == '__main__':
    app.run(port=5000)


#    https://github.com/hemansnation/
#  scheme   domain name  /route
#  http
#  https
#  ftp
#  file