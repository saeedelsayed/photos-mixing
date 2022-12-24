

from flask import Flask, render_template, request
import os;
from PIL import Image
import glob
import matplotlib.pyplot as plt
import functions as fn
skills_app = Flask(__name__,static_url_path='')


     
    

    
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
    compined_image=fn.merge("upLoads/"+fImage,"upLoads/"+fImageCropped,"upLoads/"+sImage,"upLoads/"+sImageCropped)
    plt.imsave("upLoads/result.png", compined_image)
    # im = Image.fromarray(compined_image)
    # im.save('result.png')
    return ("result.png")



if __name__ == "__main__":
    skills_app.run(port=5000)
