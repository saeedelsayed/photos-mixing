from flask import Flask, render_template, request


skills_app = Flask(__name__)


@skills_app.route("/")
def home():
    return render_template("index.html")

# route for testing axios


@skills_app.route('/merge', methods=['POST'])
def fun():
    # names of the images
    fImage=request.values['fImage']
    fImageCropped=request.values['fImageCropped']
    sImage=request.values['sImage']
    sImageCropped=request.values['sImageCropped']
    print(fImage,fImageCropped,sImage,sImageCropped)
    
    return ("generated photo name")


if __name__ == "__main__":
    skills_app.run()
