from pathlib import Path
import cv2
from image.image import Image
from image.transformer import Transformer


def main():
    img_path = (Path(__file__).parent / 'way.jpg').absolute()
    img = Image.from_file(str(img_path))
    transformer = Transformer(img)
    blurred = transformer.cannify()
    cv2.imwrite('blurred.jpg', blurred._img_data)


if __name__ == "__main__":
    main()
