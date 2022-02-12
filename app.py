from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "testkeyWUT123"

@app.route("/hello")
def index():
    flash("what's your naaaame?")
    return render_template("index.html")

@app.route("/greet", methods=["POST", "GET"])
def greet():
    flash("Hi " + str(request.form['name_input']) + ", great to see you!")
    request.form['name_input']
    return render_template("index.html")