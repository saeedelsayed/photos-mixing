from flask import Flask, render_template

skills_app = Flask(__name__)


@skills_app.route("/")
def home():
    return render_template("index.html")




if __name__ == "__main__":
    skills_app.run()

