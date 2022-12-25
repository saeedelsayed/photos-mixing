

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


@skills_app.route('/merge', methods=['POST'])
def fun():
    # names of the images
    print('saeed')
    fImage = request.values['fImage']
    # print(fImage)
    fImageCropped = request.values['fImageCropped']
    sImage = request.values['sImage']
    sImageCropped = request.values['sImageCropped']
    c = request.values['counter']
    print(fImage, fImageCropped, sImage, sImageCropped)
    compined_image = fn.merge("uploads/"+fImage, "uploads/" +
                              fImageCropped, "uploads/"+sImage, "uploads/"+sImageCropped)
    plt.imsave(f"static/result{c}.png", compined_image, cmap='gray')

    return (f"result{c}.png")


if __name__ == "__main__":
    skills_app.run(port=1919)
