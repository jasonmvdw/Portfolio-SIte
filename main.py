import requests
from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route("/")
def index():
   return render_template("index.html")

@app.route("/projects")
def projects():
   return render_template("projects.html")


@app.route("/about")
def about():
   pass


@app.route("/contact", methods = ['GET', 'POST'])
def contact():
   if request.method == "POST":
      name = request.form['name']
      email = request.form['emailAddress']
      name = request.form['message']
      return redirect("/")
   return render_template("contact.html")

app.run(debug = True)