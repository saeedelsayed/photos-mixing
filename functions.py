import numpy as np
import cv2
import matplotlib.pyplot as plt

class Manager:
    def __init__(self):
        print("Manager Constructor")
        
    def coordinate(self,image, crop):
        result = cv2.matchTemplate(image, crop, cv2.TM_SQDIFF_NORMED)
        mn, _, mnLoc, _ = cv2.minMaxLoc(result)
        MPx, MPy = mnLoc
        return MPx, MPy

    def preprocessing(self,image,crop,matrix,cropped_part,flag):
        MPx , MPy = self.coordinate(image,crop)

        result = matrix
        y ,x = crop.shape

        if(cropped_part=='inner'):
            result = np.ones(image.shape)
            if(flag==False):
                result = np.zeros(image.shape)

            result[MPy:MPy+y,MPx:MPx+x] = matrix[MPy:MPy+y,MPx:MPx+x]
        else:
            result[MPy:MPy+y,MPx:MPx+x] = 1
            if(flag==False):
                result[MPy:MPy+y,MPx:MPx+x] = 0

        return result


    def merge(self,magnitude,img1,crop1,phase,img2,crop2,imgOneCroppingCase,imgTwoCroppingCase):
        modified_magnitude = self.preprocessing(img1,crop1,magnitude,imgOneCroppingCase,True)
        modified_phase = self.preprocessing(img2,crop2,phase,imgTwoCroppingCase,False)

        combined = np.fft.ifft2(np.fft.fftshift(np.multiply(modified_magnitude,np.exp(1j*modified_phase))))
        return np.real(combined)

class Image:
    def __init__(self,  image_path):
        self.image = cv2.imread(image_path,cv2.IMREAD_GRAYSCALE)
        self.fourier_transform = self.fourier()

    def fourier(self):
        f = np.fft.fft2(self.image)
        f = np.fft.fftshift(f)
        return f

    def getMagnitude(self):
        return np.abs(self.fourier_transform)

    def getPhase(self):
        return np.angle(self.fourier_transform)

    @classmethod
    def save(cls,path, combined_image):
        plt.imsave(path, combined_image, cmap='gray')


    