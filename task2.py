import cv2
import numpy as np
import matplotlib.pyplot as plt


def display_img(img: object) -> object:
    new_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(new_img)
    plt.show()


car1 = cv2.imread('1166226.jpg')
display_img(car1)
car2 = car1.copy()
print(car2.shape)
for i in range(car2.shape[0]):
    for j in range(car2.shape[1]):
        car2[i][j][:] = (car2[i][j][0] * 0.587) + (car2[i][j][1] * 0.114) + (car2[i][j][2] * 0.2989)
display_img(car2)
