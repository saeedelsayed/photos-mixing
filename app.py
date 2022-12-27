

from flask import Flask, render_template, request
import os
from PIL import Image
import glob
import matplotlib.pyplot as plt
import functions as fn
import numpy as np

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
    global magPath
    global phasePath
    if required == '0':
        f = fn.fourier("uploads/"+image)
        mag_img = fn.getMagnitude(f)
        magPath = f"static/magImage{counter}.png"
        print(magPath)
        plt.imsave(magPath, np.log(mag_img), cmap='gray')
        return f"magImage{counter}.png"
    elif required == '1':
        f = fn.fourier("uploads/"+image)
        phase_img = fn.getPhase(f)
        phasePath = f"static/phaseImg{counter}.png"
        print(phasePath)
        plt.imsave(phasePath, phase_img, cmap='gray')
        return f"phaseImg{counter}.png"
    print(image, required)
    # return the photo name and save it on the static folder ( don't forget to use the counter with the name)


@skills_app.route('/merge', methods=['POST'])
def fun():
    # names of the images
    print('saeed')
    magImage = request.values['magnitude']
    phaseImage = request.values['phase']
    print(magImage, phaseImage)
    f = fn.fourier("uploads/"+magImage)
    mag_img = fn.getMagnitude(f)
    f = fn.fourier("uploads/"+phaseImage)
    phase_img = fn.getPhase(f)
    fImage = request.values['fImage']
    print(magImage, phaseImage)
    fImageCropped = request.values['fImageCropped']
    sImage = request.values['sImage']
    sImageCropped = request.values['sImageCropped']
    counter = request.values['counter']
    print(fImage, fImageCropped, sImage, sImageCropped)
    compined_image = fn.merge(mag_img, "static/"+fImage, "uploads/" + fImageCropped, phase_img,
                              "static/"+sImage, "uploads/"+sImageCropped)
    print('combined')
    plt.imsave(f"static/result{counter}.png", compined_image, cmap='gray')
    # i just need the generated photo name and save it on static folder
    return f'result{counter}.png'


if __name__ == "__main__":
    skills_app.run(port=3000)
