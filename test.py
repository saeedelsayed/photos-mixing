import matplotlib.pyplot as plt
import cv2
import numpy as np
import functions

f_cat = functions.fourier('cat.jpeg')

plt.imsave('mag.jpg',np.log(functions.getMagnitude(f_cat)),cmap='gray')

f_door = functions.fourier('door.jpeg')

plt.imsave('phase.jpg',functions.getPhase(f_door),cmap='gray')


combined = functions.merge(functions.getMagnitude(f_cat),'mag.jpg','mag_crop.jpg',functions.getPhase(f_door),'phase.jpg','phase_crop.jpg')

plt.imshow(combined,cmap='gray')
plt.show()


