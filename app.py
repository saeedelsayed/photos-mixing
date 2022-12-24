from flask import Flask, render_template, request


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
    from PIL import Image
    import glob
    image_list = []
    for filename in glob.glob('static/image.png'): #assuming gif
        im=Image.open(filename)
        image_list.append(im)
    print(image_list)    
    return ("generated photo name")



if __name__ == "__main__":
    skills_app.run(port=5000)
