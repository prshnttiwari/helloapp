from flask import Flask, render_template,request,flash

app = Flask(__name__)
app.secret_key = "kjnkdjvsldjs_sdfjsb442kjbxdfsd"

@app.route("/hello")
def index():
    flash("whats your name?")
    return render_template("index.html")

@app.route("/greet", methods=["POST","GET"])
def greet():
    flash("hi " + str(request.form['name_input']) + ", great to see you!")
    return render_template("index.html")
