from flask import Flask, render_template, request
from datetime import date, datetime

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
	#aktuální datum
	date = datetime.now().strftime("%d. %m. %Y")
	password = request.args.get("password")
	if password == "tajneheslo":
		return "Tajné heslo je správné!"
	elif password:
		return "Tajné heslo je nesprávné!"
	name=request.args.get("name")
	surname=request.args.get("surname")


	return render_template("page.html", date=date, name=name, surname=surname)

@app.route("/pozdrav-post", methods=["POST", "GET"])
def pozdrav_post():
	#aktuální datum
	date = datetime.now().strftime("%d. %m. %Y")

	name = None
	surname = None
	tajna_zprava = None
	chyba = None

	if request.method == "POST":
		name = request.form.get("name")
		surname = request.form.get("surname")
		password = request.form.get("password")

		if not name:
			chyba = "Jméno nesmí být prázdné!"
		elif len(name) > 50:
			chyba = "Jméno je příliš dlouhé (max. 50 znaků)!"
		elif password == "tajneheslo":
			tajna_zprava = "Tajné heslo je správné, krejzy!"
		elif password:
			chyba = "Tajné heslo je nesprávné!"

	return render_template("pozdrav_post.html", date=date, name=name, surname=surname, tajna_zprava=tajna_zprava, chyba=chyba)

if __name__=="__main__":
	app.run(debug=True)