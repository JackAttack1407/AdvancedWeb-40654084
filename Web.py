from flask import Flask, render_template

app = Flask(__name__)


##index page
@app.route("/")
def index():
	return render_template("index.html")



##overview pages
@app.route("/Classes")
def classes():
	return render_template("ClassPagesOverview.html")

@app.route("/LorePages")
def lorepages():
	return render_template("LorePagesOverview.html")


@app.route("/RaidGuides")
def raidpages():
	return render_template("RaidGuideOverview.html")



##classes
@app.route("/Classes/Titan")
def titan():
	return render_template("ClassPages/Titan(class).html")

@app.route("/Classes/Hunter")
def hunter():
	return render_template("ClassPages/Hunter(class).html")

@app.route("/Classes/Warlock")
def warlock():
	return render_template("ClassPages/Warlock(class).html")



##lore pages
@app.route("/LorePages/DeepstoneCrypt")
def cryptlore():
	return render_template("LorePages/CryptLore.html")

@app.route("/LorePages/GardenOfSalvation")
def gardenlore():
	return render_template("LorePages/GardenLore.html")

@app.route("/LorePages/LastWish")
def lastwishlore():
	return render_template("LorePages/LastWishLore.html")

@app.route("/LorePages/VOG")
def VOGlore():
	return render_template("LorePages/VOGLore.html")




##raid guides
@app.route("/RaidGuides/DeepstoneCrypt")
def cryptguide():
	return render_template("RaidPages/CryptGuide.html")

@app.route("/RaidGuides/GardenOfSalvation")
def gardenguide():
	return render_template("RaidPages/GardenGuide.html")

@app.route("/RaidGuides/LastWish")
def lastwishguide():
	return render_template("RaidPages/LastWishGuide.html")

@app.route("/RaidGuides/VOG")
def VOGguide():
	return render_template("RaidPages/VOGGuide.html")




## reference page
@app.route("/ReferencePage")
def refpage():
	return render_template("ReferencePage.html")
