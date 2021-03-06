import pyxel


class Engine:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.x = 100
        self.y = 100
        self.xspeed = 1
        self.yspeed = 3.3

    def update(self):
        self.x = self.x + self.xspeed
        self.y = self.y + self.yspeed

        if self.x > self.width or self.x < 0:
            self.xspeed = -self.xspeed
        if self.y > self.height or self.y < 0:
            self.yspeed = -self.yspeed


class App:
    def __init__(self):
        pyxel.init(160, 120)
        self.engine = Engine(pyxel.width, pyxel.height)
        pyxel.run(self.update, self.draw)

    def update(self):
        self.engine.update()

    def draw(self):
        pyxel.cls(0)
        pyxel.circ(self.engine.x, self.engine.y, 8, 9)


if __name__ == '__main__':
    App()
