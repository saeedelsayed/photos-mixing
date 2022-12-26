import cv2
import numpy as np
import matplotlib.pyplot as plt
from pylab import *
import matplotlib.cm as cm


def match(image, crop):
    result = cv2.matchTemplate(image, crop, cv2.TM_SQDIFF_NORMED)
    mn, _, mnLoc, _ = cv2.minMaxLoc(result)
    MPx, MPy = mnLoc
    return MPx, MPy


def preprocessing(image_path, crop_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    crop = cv2.imread(crop_path, cv2.IMREAD_GRAYSCALE)

    MPx, MPy = match(image, crop)
    y, x = crop.shape

    f = np.fft.fft2(image)
    f = np.fft.fftshift(f)
    magnitude_spectrum = np.abs(f)
    phase_spectrum = np.angle(f)

    arr = np.zeros(image.shape, dtype=np.uint8)
    arr[MPy:MPy+y, MPx:MPx+x] = 1

    magnitude_spectrum = np.multiply(arr, magnitude_spectrum)
    phase_spectrum = np.multiply(arr, phase_spectrum)

    return magnitude_spectrum, phase_spectrum


def merge(first_image_path, first_crop_path, second_image_path, second_crop_path, counter):
    first_image_magnitude, first_image_phase = preprocessing(
        first_image_path, first_crop_path)
    second_image_magnitude, second_image_phase = preprocessing(
        second_image_path, second_crop_path)

    first_original = cv2.imread(first_image_path, cv2.IMREAD_GRAYSCALE)
    second_original = cv2.imread(second_image_path, cv2.IMREAD_GRAYSCALE)

    # print(first_image.shape)
    # print(first_original.shape)
    # print(second_image.shape)
    # print(second_original.shape)
    #first_image_magnitude, first_image_phase = getPhaseMagnitude(first_image)
    # second_image_magnitude, second_image_phase = getPhaseMagnitude(
    # second_image)
    # imshow(first_image_magnitude)

    plt.imsave(f'static/magImage{counter}.png', np.real(np.fft.ifft2(np.multiply(
        first_image_magnitude, 1))), cmap='gray')

    plt.imsave(f'static/phaseImg{counter}.png', np.real(np.fft.ifft2(np.multiply(
        1, np.exp(1j*second_image_phase)))), cmap='gray')

    combined = np.real(np.fft.ifft2(np.multiply(
        first_image_magnitude, np.exp(1j*second_image_phase))))
    return combined
