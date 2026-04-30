from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
	#aktuální datum
	date = datetime.now().strftime("%d. %m. %Y")

	name=request.args.get("name")

	return render_template("page.html", date=date, name=name)

if __name__=="__main__":
	app.run(debug=True)