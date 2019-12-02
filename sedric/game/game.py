import time
import cv2
import numpy as np

VIEWPORT = {"top": 40, "left": 0, "width": 1280, "height": 720}


class Game:
    def __init__(self, sct):
        self.sct = sct

    def grab(self):
        return np.array(self.sct.grab(VIEWPORT))

    def mainloop(self):
        while True:
            last_time = time.time()
            grayscale = cv2.cvtColor(self.grab(), cv2.COLOR_BGRA2GRAY)
            blurred = cv2.GaussianBlur(grayscale, (5, 5), 0)
            canny = cv2.Canny(blurred, 40, 120)
            cv2.imshow('test', canny)
            print("fps: {}".format(1 / (time.time() - last_time)))

            if self._exit:
                cv2.destroyAllWindows()
                break

    @property
    def _exit(self):
        return cv2.waitKey(25) & 0xFF == ord('q')
