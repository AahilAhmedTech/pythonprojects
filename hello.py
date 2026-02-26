from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, GitHub! This is a Python-only web app."

@app.route("/about")
def about():
    return "Learning Flask without separate HTML files."

if __name__ == "__main__":
    app.run(debug=True)
