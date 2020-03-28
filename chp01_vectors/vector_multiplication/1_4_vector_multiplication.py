import pyxel

from chp01_vectors.bouncingball_vectors.pyvector import Vector


class Engine:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.position = Vector(0, 0)
        self.center = Vector(width / 2, height / 2)

    def update(self, x, y):
        self.position.x = x*0.5
        self.position.y = y*0.5
        #self.position.mult(0.5)
        print(f'{self.position.x} {self.position.y} {pyxel.mouse_x} {pyxel.mouse_y}')


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
            self.engine.position.x,
            self.engine.position.y,
            8
        )


if __name__ == '__main__':
    App()
