import numpy as np
import cv2

def fourier(image_path):
    image = cv2.imread(image_path,cv2.IMREAD_GRAYSCALE)
    f = np.fft.fft2(image)
    return f

def getMagnitude(f):
    return np.abs(f)

def getPhase(f):
    return np.angle(f)

def match(image, crop):
    result = cv2.matchTemplate(image, crop, cv2.TM_SQDIFF_NORMED)
    mn, _, mnLoc, _ = cv2.minMaxLoc(result)
    MPx, MPy = mnLoc
    return MPx, MPy

def preprocessing(image,crop,matrix,flag):
    MPx , MPy = match(image,crop)

    y ,x = crop.shape
    result = np.ones(image.shape)

    if(flag==False):
        result = np.zeros(image.shape)

    result[MPy:MPy+y,MPx:MPx+x] = matrix[MPy:MPy+y,MPx:MPx+x]
    return result


def merge(magnitude,img1_path,crop1_path,phase,img2_path,crop2_path):
    img1 = cv2.imread(img1_path,cv2.IMREAD_GRAYSCALE)
    crop1 = cv2.imread(crop1_path,cv2.IMREAD_GRAYSCALE)

    img2 = cv2.imread(img2_path,cv2.IMREAD_GRAYSCALE)
    crop2= cv2.imread(crop2_path,cv2.IMREAD_GRAYSCALE)

    modified_magnitude = preprocessing(img1,crop1,magnitude,True)
    modified_phase = preprocessing(img2,crop2,phase,False)

    combined = np.fft.ifft2(np.multiply(modified_magnitude,np.exp(1j*modified_phase)))
    return np.real(combined)

