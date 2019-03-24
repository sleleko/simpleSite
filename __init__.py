from flask import Flask
app = Flask(__name__)
@app.route("/")
def index():
    return "Главная страница"
if __name__ == "__main__":
    app.run(debug=True)

@app.route("/about")
def about():
    return "Обо мне"

