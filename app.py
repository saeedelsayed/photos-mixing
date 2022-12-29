

from flask import Flask, render_template, request
import os
from PIL import Image
import glob
import matplotlib.pyplot as plt

import numpy as np
from functions import Manager,Image


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
    if required == '0':
        first_original=Image("uploads/"+image)
        magnitude = first_original.getMagnitude()
        magPath = f"static/magImage{counter}.png"
        Image.save(magPath,np.log(magnitude))
        return f"magImage{counter}.png"
    elif required == '1':
        second_original=Image("uploads/"+image)
        phase = second_original.getPhase()
        phasePath = f"static/phaseImg{counter}.png"
        Image.save(phasePath,phase)
        return f"phaseImg{counter}.png"
    # return the photo name and save it on the static folder ( don't forget to use the counter with the name)


@skills_app.route('/merge', methods=['POST'])
def fun():
    # names of the images
    first_original = request.values['firstOriginal']
    second_original = request.values['secondOriginal']
    fImage = request.values['fImage']
    fImageCropped = request.values['fImageCropped']
    sImage = request.values['sImage']
    sImageCropped = request.values['sImageCropped']
    counter = request.values['counter']

    f_original = Image("uploads/"+first_original)
    f_magnitude = f_original.getMagnitude()

    s_original=Image("uploads/"+second_original)
    s_phase = s_original.getPhase()

    f_Image = Image("static/"+fImage)
    f_ImageCropped = Image("uploads/"+fImageCropped)
    s_Image = Image("static/"+sImage)
    s_ImageCropped = Image("uploads/"+sImageCropped)
    manager = Manager() 
    combined_image=manager.merge(f_magnitude, f_Image.image, f_ImageCropped.image, s_phase,
                              s_Image.image, s_ImageCropped.image)

    Image.save(f"static/result{counter}.png",combined_image)
    # i just need the generated photo name and save it on static folder
    return f'result{counter}.png'


if __name__ == "__main__":
    skills_app.run(port=4000)
