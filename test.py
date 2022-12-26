import functions
import matplotlib.pyplot as plt
import numpy as np

first_mag, first_phase = functions.preprocessing('cat.jpeg', 'cat_crop.jpeg')

second_mag, second_phase = functions.preprocessing(
    'door.jpeg', 'door_crop.jpeg')

combined = np.real(np.fft.ifft2(
    np.multiply(second_mag, np.exp(1j*first_phase))))


plt.imshow(np.log(second_mag), cmap='gray')
plt.imshow(first_phase, cmap='gray')

#plt.imshow(combined, cmap='gray')

plt.show()
