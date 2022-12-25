import functions
import matplotlib.pyplot as plt

image = functions.merge('s.jpg', 's.jpg', 'f.jpg', 'f.jpg')

plt.imshow(image, cmap='gray')

plt.show()
