from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Hello, GitHub!</h1>
    <p>Learning GitHub Desktop and VS Code!</p>
    <p>This is my first Flask web app.</p>
    """

if __name__ == "__main__":
    app.run(debug=True)
