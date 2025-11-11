from flask import Flask, render_template

app = Flask(__name__)


##index page
@app.route("/")
def index():
	return render_template("index.html")



##overview pages
@app.route("/Classes")
def classes():
	with open("Templates/ClassPagesOverview.html") as f:
		return f.read()

@app.route("/LorePages")
def lorepages():
	with open("Templates/LorePagesOverview.html") as f:
		return f.read()


@app.route("/RaidGuides")
def raidpages():
	with open("Templates/RaidGuideOverview.html") as f:
		return f.read()



##classes
@app.route("/Classes/Titan")
def titan():
	with open("Templates/ClassPages/Titan(class).html") as f:
		return f.read()

@app.route("/Classes/Hunter")
def hunter():
	with open("Templates/ClassPages/Hunter(class).html") as f:
		return f.read()

@app.route("/Classes/Warlock")
def warlock():
	with open("Templates/ClassPages/Warlock(class).html") as f:
		return f.read()



##lore pages
@app.route("/LorePages/DeepstoneCrypt")
def cryptlore():
	with open("Templates/LorePages/CryptLore.html") as f:
		return f.read()

@app.route("/LorePages/GardenOfSalvation")
def gardenlore():
	with open("Templates/LorePages/GardenLore.html") as f:
		return f.read()

@app.route("/LorePages/LastWish")
def lastwishlore():
	with open("Templates/LorePages/LastWishLore.html") as f:
		return f.read()

@app.route("/LorePages/VOG")
def VOGlore():
	with open("Templates/LorePages/VOGLore.html") as f:
		return f.read()




##raid guides
@app.route("/RaidGuides/DeepstoneCrypt")
def cryptguide():
	with open("Templates/RaidPages/CryptGuide.html") as f:
		return f.read()

@app.route("/RaidGuides/GardenOfSalvation")
def gardenguide():
	with open("Templates/RaidPages/GardenGuide.html") as f:
		return f.read()

@app.route("/RaidGuides/LastWish")
def lastwishguide():
	with open("Templates/RaidPages/LastWishGuide.html") as f:
		return f.read()

@app.route("/RaidGuides/VOG")
def VOGguide():
	with open("Templates/RaidPages/VOGGuide.html") as f:
		return f.read()




## reference page
@app.route("/ReferencePage")
def refpage():
	with open("Templates/ReferencePage.html") as f:
		return f.read()
