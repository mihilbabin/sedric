from mss import mss

import game


def main():
    with mss() as sct:
        g = game.Game(sct)
        g.mainloop()


if __name__ == "__main__":
    main()
