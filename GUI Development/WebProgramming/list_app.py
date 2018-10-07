from flask import Flask, render_template
app=Flask(__name__)
@app.route("/")
def index():
    names=["alice", "Bob", "charlie"]
    return render_template("list.html", names=names)


