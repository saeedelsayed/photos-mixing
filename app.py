from flask import Flask, render_template, request


skills_app = Flask(__name__)


@skills_app.route("/")
def home():
    return render_template("index.html")

# route for testing axios


@skills_app.route('/merge', methods=['POST'])
def fun():
    # print('diaa')
    # print(request.form['formData'])
    # imageFile = request.files.get('file','')
    # print(request.files)
    return (request.files)


if __name__ == "__main__":
    skills_app.run()
