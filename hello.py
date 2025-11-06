from flask import Flask

app = Flask(__name__)


##index page
@app.route("/")
def hello():
	with open("Templates/index.html") as f:
		return f.read()


##classes
@app.route("/Titan(class)")
def titan():
	with open("Templates/ClassPages/Titan(class).html") as f:
		return f.read()

@app.route("/Hunter(class)")
def hunter():
	with open("Templates/ClassPages/Hunter(class).html") as f:
		return f.read()

@app.route("/Warlock(class)")
def warlock():
	with open("Templates/ClassPages/Warlock(class).html") as f:
		return f.read()

##lore pages
@app.route("/CryptLore")
def cryptlore():
	with open("Templates/LorePages/CryptLore.html") as f:
		return f.read()

@app.route("/GardenLore")
def gardenlore():
	with open("Templates/LorePages/GardenLore.html") as f:
		return f.read()

@app.route("/LastWishLore")
def lastwishlore():
	with open("Templates/LorePages/LastWishLore.html") as f:
		return f.read()

@app.route("/VOGLore")
def VOGlore():
	with open("Templates/LorePages/VOGLore.html") as f:
		return f.read()

##raid guides
@app.route("/CryptGuide")
def cryptguide():
	with open("Templates/RaidPages/CryptGuide.html") as f:
		return f.read()

@app.route("/GardenGuide")
def gardenguide():
	with open("Templates/RaidPages/GardenGuide.html") as f:
		return f.read()

@app.route("/LastWishGuide")
def lastwishguide():
	with open("Templates/RaidPages/LastWishGuide.html") as f:
		return f.read()

@app.route("/VOGGuide")
def VOGguide():
	with open("Templates/RaidPages/VOGGuide.html") as f:
		return f.read()

## reference page
@app.route("/ReferencePage")
def refpage():
	with open("Templates/ReferencePage.html") as f:
		return f.read()
