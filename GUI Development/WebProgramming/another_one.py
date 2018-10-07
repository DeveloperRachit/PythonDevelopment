from flask import Flask, render_template

app=Flask(__name__)
@app.route("/")
def index():
    return render_template("index1.html")

@app.route("/more1")
def more1():
     return render_template("more1.html")