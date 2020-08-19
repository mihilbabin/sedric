import time
from pathlib import Path

import cv2
import numpy as np
from imutils.video import FileVideoStream, FPS

from image import utils
from image.image import Image
from image.transformer import Transformer
from base import region


def main():
    vid = (Path(__file__).parent / 'test.mp4').absolute()
    stream = FileVideoStream(str(vid), queue_size=100).start()
    time.sleep(1)

    while stream.more():
        img_data = stream.read()
        if img_data is None:
            break
        img = Image(img_data)
        transformed = Transformer(img)
        image = transformed.cannify()
        cropped_img = region(image)
        lines = cv2.HoughLinesP(cropped_img.raw, 2, np.pi / 180,
                                100, np.array([]), minLineLength=40, maxLineGap=5)
        avg_lines = utils.average_slope_intercept(img, lines)
        lines_image = img.display_lines(avg_lines)
        combined = img.combine(lines_image)
        cv2.imshow('', combined.raw)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()
    stream.stop()


if __name__ == "__main__":
    main()
