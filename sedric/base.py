from pathlib import Path
from image.image import Image
from image.transformer import Transformer
from image import utils
import numpy as np
import cv2


def region(image: Image) -> Image:
    width, height = image.dims
    triangle = np.array([(200, height), (1100, height), (550, 250)])
    mask = np.zeros_like(image.raw)
    cv2.fillPoly(mask, [triangle], 255)
    return Image(cv2.bitwise_and(image.raw, mask))


def main():
    img_path = (Path(__file__).parent / 'lanes.jpg').absolute()
    img = Image.from_file(str(img_path))
    transformed = Transformer(img)
    image = transformed.cannify()
    cropped_img = region(image)
    lines = cv2.HoughLinesP(cropped_img.raw, 2, np.pi / 180,
                            100, np.array([]), minLineLength=40, maxLineGap=5)
    avg_lines = utils.average_slope_intercept(img, lines)
    lines_image = img.display_lines(avg_lines)
    combined = img.combine(lines_image)
    combined.show(stream=False)


if __name__ == "__main__":
    main()
