import cv2


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
