from flask import Flask, render_template
app=Flask(__name__)

@app.route("/<string:name>")
def index(name):

    headline=f"Hello!{name}"
    return render_template("new.html", headline=headline)

