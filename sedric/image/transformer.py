from .image import Image
from .utils import ImageConverter


class Transformer:
    def __init__(self, image: Image):
        self._image = image

    @property
    def image(self):
        return self._image

    @property
    def data(self):
        return self._image.raw

    def cannify(self, kernel: tuple = (5, 5), low: int = 40, high: int = 120) -> Image:
        raw_image = ImageConverter.grayscale(self.data)
        raw_image = ImageConverter.blur(raw_image, kernel)
        return Image(ImageConverter.canny(raw_image, low, high))

    def blur(self, kernel: tuple = (5, 5)) -> Image:
        return Image(ImageConverter.blur(self.data, kernel))

    def grayscale(self) -> Image:
        return Image(ImageConverter.grayscale(self.data))

    def canny(self, low: int = 40, high: int = 120) -> Image:
        return Image(ImageConverter.canny(self.data, low, high))
