from pathlib import Path
from image import Image


def main():
    img_path = (Path(__file__).parent / 'lanes.jpg').absolute()
    img = Image.from_file(str(img_path))
    grayscale = img.grayscale()
    blurred = grayscale.blur()
    blurred.show('blurred')
    grayscale.show('grayscale')
    img.show('Original')


if __name__ == "__main__":
    main()
