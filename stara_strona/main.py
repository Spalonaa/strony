from flask import Flask, render_template
from random import randint

app = Flask(__name__)

@app.route("/es")
def es():
    return render_template("index.html", losowa=randint(1, 100))

@app.route("/")
def hello():
    return "<h1>Witaj Świecie!</h1><a href='/test'>Przejdź do strony testowej</a>"

@app.route("/test")
def test():
    return f"<p>Strona testowa. Losowa liczba: {randint(1, 100)}</p><a href='/'>Cofnij się</a>"

app.run(debug=True)