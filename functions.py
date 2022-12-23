import cv2
import numpy as np

def match(image,crop):
    result = cv2.matchTemplate(image,crop, cv2.TM_SQDIFF_NORMED)
    mn,_,mnLoc,_ = cv2.minMaxLoc(result)
    MPx,MPy = mnLoc
    return MPx,MPy


def preprocessing(image_path,crop_path):
    image = cv2.imread(image_path,cv2.IMREAD_GRAYSCALE)
    crop = cv2.imread(crop_path,cv2.IMREAD_GRAYSCALE)

    MPx,MPy = match(image,crop)
    y ,x = crop.shape

    result_image = np.zeros(image.shape,dtype=np.uint8)
    result_image[MPy:MPy+y,MPx:MPx+x] = image[MPy:MPy+y,MPx:MPx+x]
    return result_image

def getPhaseMagnitude(image):
    f = np.fft.fft2(image)
    magnitude_spectrum = np.abs(f)
    phase_spectrum = np.angle(f)
    return magnitude_spectrum,phase_spectrum

def merge(first_image_path,first_crop_path,second_image_path,second_crop_path):
    first_image = preprocessing(first_image_path,first_crop_path)
    second_image = preprocessing(second_image_path,second_crop_path)

    first_image = cv2.resize(first_image,(1000,1000))
    second_image = cv2.resize(second_image,(1000,1000))

    first_image_magnitude,first_image_phase = getPhaseMagnitude(first_image)
    second_image_magnitude,second_image_phase = getPhaseMagnitude(second_image)

    combined = np.real(np.fft.ifft2(np.multiply(first_image_magnitude, np.exp(1j*second_image_phase))))
    return combined