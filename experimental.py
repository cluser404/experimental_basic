from flask import Flask

app = Flask(__name__)


@app.route("/<username>/<path:path>")
def show_username(username, path):
	prompt = "user {} loged in <br> accesing path: {}".format(username, str(path))
	return(prompt)

app.run(debug=True)