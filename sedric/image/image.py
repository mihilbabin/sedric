from __future__ import annotations

import cv2
import numpy as np


class Image:
    def __init__(self, data):
        self._img_data = data

    def show(self, title: str = 'Image', stream: bool = True):
        cv2.imshow(title, self._img_data)
        if not stream:
            cv2.waitKey(0)

    def display_lines(self, lines: np.array) -> Image:
        with_lines = np.zeros_like(self.raw)
        if lines is not None:
            for line in lines:
                x1, y1, x2, y2 = line.reshape(4)
                cv2.line(with_lines, (x1, y1), (x2, y2), (255, 0, 0), 10)
        return Image(with_lines)

    def combine(self, image: Image, w1=0.8, w2=1, gamma=1) -> Image:
        return Image(cv2.addWeighted(self.raw, w1, image.raw, w2, gamma))

    @property
    def raw(self):
        return self._img_data

    @property
    def dims(self) -> tuple:
        return (self._img_data.shape[1], self._img_data.shape[0])

    @staticmethod
    def from_file(path: str) -> Image:
        return Image(Image._cv2_read(path))

    @staticmethod
    def _cv2_read(path: str):
        return cv2.imread(path)
