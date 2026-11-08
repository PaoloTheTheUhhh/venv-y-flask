from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<h1> Pan Con Chocolate' \
    ' <a href="/random_fact">¡Ver un dato aleatorio!</a>' \
    ' <a href="/">¡Pagina Principal!</a></h1>'
@app.route("/")
def home():
    return "<h1>Home page</h1>"
@app.route("/random_fact")

def random_fact():
    return "<h1>Random Fact</h1>"
app.run(debug=True)