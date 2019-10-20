import cv2


class Image:
    def __init__(self, path: str):
        self.path = path
        self._img_data = cv2.imread(path)

    def show(self):
        cv2.imshow(self.path, self._img_data)
        cv2.waitKey(0)
