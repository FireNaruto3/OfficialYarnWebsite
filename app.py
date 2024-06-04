from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods = ["GET","POST"])
def homePage():
    return render_template("home.html")

@app.route("/questions.html", methods = ["GET", "POST"])
def questionPage():
    return render_template("questions.html")

if(__name__ == '__main__'):
    app.run(debug = True)
