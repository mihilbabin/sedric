from __future__ import annotations

import cv2


class Image:
    def __init__(self, data):
        self._img_data = data

    def show(self, title: str = 'Image'):
        cv2.imshow(title, self._img_data)
        cv2.waitKey(0)

    def blur(self) -> Image:
        return Image(self._cv2_blur())

    def grayscale(self) -> Image:
        return Image(self._cv2_grayscale())

    @staticmethod
    def from_file(path: str) -> Image:
        return Image(Image._cv2_read(path))

    @staticmethod
    def _cv2_read(path: str):
        return cv2.imread(path)

    def _cv2_grayscale(self):
        return cv2.cvtColor(self._img_data, cv2.COLOR_RGB2GRAY)

    def _cv2_blur(self):
        return cv2.GaussianBlur(self._img_data, (5, 5), 0)
