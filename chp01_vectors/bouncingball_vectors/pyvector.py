import math


class Vector:
    def __init__(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z

    def __sub__(self, other):
        self.x -= other.x
        self.y -= other.y
        self.z -= other.z

    def mul(self, scalar):
        self.x *= scalar
        self.y *= scalar
        self.z *= scalar

    def div(self, scalar):
        self.x /= scalar
        self.y /= scalar
        self.z /= scalar

    def distance(self, vector):
        dx = self.x - vector.x
        dy = self.y - vector.y
        dz = self.z - vector.z
        return math.sqrt(dx**2 + dy**2 + dz**2)

    def __matmul__(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z
