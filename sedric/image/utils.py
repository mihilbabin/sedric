import cv2
import numpy as np


def average_slope_intercept(image, lines: np.array) -> np.array:
    left, right = [], []
    for line in lines:
        x1, y1, x2, y2 = line.reshape(4)
        params = np.polyfit((x1, x2), (y1, y2), 1)
        slope, intercept = params[0], params[1]
        (left if slope < 0 else right).append((slope, intercept))
    left_line, right_line = [0, 0, 0, 0], [0, 0, 0, 0]
    if left:
        left_line = line_coordinates(image, np.average(left, 0))
    if right:
        right_line = line_coordinates(image, np.average(right, 0))
    return np.array([left_line, right_line])


def line_coordinates(image, line_params):
    slope, intercept = line_params
    y1 = image.dims[1]
    y2 = int(y1*3/5)
    x1 = int((y1 - intercept) / slope)
    x2 = int((y2 - intercept) / slope)
    return np.array([x1, y1, x2, y2])


class ImageConverter:
    @staticmethod
    def grayscale(image_data):
        return cv2.cvtColor(image_data, cv2.COLOR_RGB2GRAY)

    @staticmethod
    def blur(image_data, kernel: tuple):
        return cv2.GaussianBlur(image_data, kernel, 0)

    @staticmethod
    def canny(image_data, low: int, high: int):
        return cv2.Canny(image_data, low, high)
