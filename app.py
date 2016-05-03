from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
	return "Home"

@app.route("/help")
def help():
	return "Help"

if __name__ == "__main__":
	app.run()