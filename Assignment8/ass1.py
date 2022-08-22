import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np
path = "tiger.jpeg"
img = cv.imread(path) 
print(img.shape, img.size)
plt.imshow(img)
tmp_red = np.copy(img)
tmp_red[:,:, 1] = [0]
tmp_red[:, :, 2] = [0]
plt.imshow(tmp_red)
tmp_green = np.copy(img)
tmp_green[:,:, 0] = [0]
tmp_green[:, :, 2] = [0]
plt.imshow(tmp_green)



