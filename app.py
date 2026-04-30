from flask import Flask, render_template, request
from datetime import datetime

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

	name=request.form.get("name")
	surname=request.form.get("surname")


	return render_template("pozdrav_post.html", date=date, name=name, surname=surname)

if __name__=="__main__":
	app.run(debug=True)