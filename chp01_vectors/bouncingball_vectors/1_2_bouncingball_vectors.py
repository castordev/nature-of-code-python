import pyxel

from chp01_vectors.bouncingball_vectors.pyvector import Vector


class Engine:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.location = Vector(100, 100)
        self.velocity = Vector(2.5, 5)

    def update(self):
        self.location.add(self.velocity)

        if self.location.x > self.width or self.location.x < 0:
            self.velocity.x = - self.velocity.x
        if self.location.y > self.height or self.location.y < 0:
            self.velocity.y = - self.velocity.y


class App:
    def __init__(self):
        pyxel.init(160, 120)
        self.engine = Engine(pyxel.width, pyxel.height)
        pyxel.run(self.update, self.draw)

    def update(self):
        self.engine.update()

    def draw(self):
        pyxel.cls(0)
        pyxel.circ(self.engine.location.x, self.engine.location.y, 8, 9)


if __name__ == '__main__':
    App()
