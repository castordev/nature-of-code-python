import pyxel

from chp01_vectors.bouncingball_vectors.pyvector import Vector


class Engine:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.mouse = Vector(0, 0)
        self.center = Vector(width / 2, height / 2)

    def update(self, x, y):
        self.mouse.x = x
        self.mouse.y = y


class App:
    def __init__(self):
        pyxel.init(160, 120)
        pyxel.mouse(True)
        self.engine = Engine(pyxel.width, pyxel.height)
        pyxel.run(self.update, self.draw)

    def update(self):
        self.engine.update(pyxel.mouse_x, pyxel.mouse_y)

    def draw(self):
        pyxel.cls(0)
        pyxel.line(
            self.engine.center.x,
            self.engine.center.y,
            self.engine.mouse.x,
            self.engine.mouse.y,
            8
        )


if __name__ == '__main__':
    App()
