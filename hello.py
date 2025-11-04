from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
	with open("Pages/index.html") as f:
		return f.read()