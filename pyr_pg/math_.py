"""
    pyr_pg's math libary
    (c) 2025 Spyro24
"""
import random
import math

def interpolateVector(start: tuple[int, int], end: tuple[int, int], time: float)->tuple[int, int]:
    "get a interpolated vector from two vectors and the time with a simple LERP"
    startX, startY = start
    endX, endY = end
    return startX + time * (endX - startX), startY + time * (endY - startY)

class PerlinNoise2D:
    def __init__(self, seed=0):
        random.seed(seed)
        self.p = list(range(256))
        random.shuffle(self.p)
        self.p += self.p  # duplicate for overflow (why?)

    def fade(self, t):
        return t * t * t * (t * (t * 6 - 15) + 10)

    def lerp(self, a, b, t):
        return a + t * (b - a)

    def grad(self, hash_val, x, y):
        h = hash_val & 3
        u = x if h < 2 else y
        v = y if h < 2 else x
        return (u if (h & 1) == 0 else -u) + (v if (h & 2) == 0 else -v)

    def noise(self, x, y):
        X = int(math.floor(x)) & 255
        Y = int(math.floor(y)) & 255
        x -= math.floor(x)
        y -= math.floor(y)
        u, v = self.fade(x), self.fade(y)

        A = self.p[X] + Y
        B = self.p[X + 1] + Y

        n00 = self.grad(self.p[A], x, y)
        n01 = self.grad(self.p[A + 1], x, y - 1)
        n10 = self.grad(self.p[B], x - 1, y)
        n11 = self.grad(self.p[B + 1], x - 1, y - 1)

        x1 = self.lerp(n00, n10, u)
        x2 = self.lerp(n01, n11, u)
        return (self.lerp(x1, x2, v) + 1) / 2  # Map result from [-1,1] to [0,1]