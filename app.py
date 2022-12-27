

from flask import Flask, render_template, request
import os
from PIL import Image
import glob
import matplotlib.pyplot as plt
import functions as fn
skills_app = Flask(__name__, static_url_path='')


@skills_app.route("/")
def home():
    return render_template("index.html")

# route for testing axios


@skills_app.route('/generate', methods=['POST'])
def generate():
    image = request.values['imgName']
    # zero means i need magnitude image, one means i need phase image
    required = request.values['required']
    counter = request.values['counter']
    print(image, required)
    # return the photo name and save it on the static folder ( don't forget to use the counter with the name)
    return "photoname"


@skills_app.route('/merge', methods=['POST'])
def fun():
    # names of the images
    print('saeed')
    fImage = request.values['fImage']
    print(fImage)
    fImageCropped = request.values['fImageCropped']
    sImage = request.values['sImage']
    sImageCropped = request.values['sImageCropped']
    counter = request.values['counter']
    print(fImage, fImageCropped, sImage, sImageCropped)
    compined_image = fn.merge("uploads/"+fImage, "uploads/" +
                              fImageCropped, "uploads/"+sImage, "uploads/"+sImageCropped, counter)
    print('combined')
    plt.imsave(f"static/result{counter}.png", compined_image, cmap='gray')
    # i just need the generated photo name and save it on static folder
    return ([f"result{counter}.png", f'magImage{counter}.png', f'phaseImg{counter}.png'])


if __name__ == "__main__":
    skills_app.run(port=3000)
