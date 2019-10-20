from pathlib import Path
from image import Image


def main():
    img_path = Path(__file__).parent / 'lanes.jpg'
    img = Image(str(img_path.absolute()))
    img.show()


if __name__ == "__main__":
    main()
