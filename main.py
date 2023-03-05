from matplotlib import image
import matplotlib.pyplot as plt
import numpy as np


def get_image():
    primary_img = input("Enter directory: ")
    matrix_img = image.imread(primary_img)
    return matrix_img


def create_gray_image(primary_img):
    for i in range(i_index):
        for j in range(j_index):
            if np.any(primary_img[i][j] < 240):
                gray_img[i][j] = (169, 169, 169)
    return gray_img


def create_shear_image(img):
    for i in range(i_index):
        for j in range(j_index):
            shear_i_index = i
            shear_j_index = int(0.2 * i + j)
            shear_img[shear_i_index, shear_j_index] = img[i][j]
    return shear_img


def crate_result_image(img):
    for i in range(i_index):
        for j in range(j_index + offset):
            if j >= j_index:
                result_img[i][j] = img[i][j]
            elif j < j_index:
                if np.any(primary_image[i][j] < 240):
                    result_img[i][j] = primary_image[i][j]
                elif np.all(img[i][j] == 169):
                    result_img[i][j] = img[i][j]
    return result_img


if __name__ == '__main__':
    primary_image = get_image()
    i_index = primary_image.shape[0]
    j_index = primary_image.shape[1]
    offset = int(primary_image.shape[1] * 0.2)
    gray_img = np.full([i_index, j_index, 3], [255, 255, 255])
    shear_img = np.full([i_index, j_index + offset, 3], [255, 255, 255])
    result_img = np.full([i_index, j_index + offset, 3], [255, 255, 255])
    gray_image = create_gray_image(primary_image)
    shear_image = create_shear_image(gray_image)
    result_image = crate_result_image(shear_image)
    plt.imshow(result_image)
    plt.show()
