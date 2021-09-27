import math


class Vector:

    def __init__(self, x_, y_):
        self.x = x_
        self.y = y_

    def set(self, x, y):
        self.x = x
        self.y = y

    def get(self):
        return self.x, self.y

    def add(self, n_vector):
        self.x += n_vector.x
        self.y += n_vector.y

    def sub(self, n_vector):
        self.x -= n_vector.x
        self.y -= n_vector.y

    def mul(self, value):
        self.x *= value
        self.y *= value

    def div(self, value):
        self.x /= value
        self.y /= value

    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def normalize(self):
        mag = self.magnitude()
        if mag != 0 and mag != 1:
            self.div(mag)

    def limit(self, value):
        if self.magnitude() > value:
            self.normalize()
            self.mul(value)

    def set_mag(self, value):
        self.normalize()
        self.mul(value)

    @staticmethod
    def div_s(vector_, value):
        return Vector(vector_.x / value, vector_.y / value)

    @staticmethod
    def sub_s(vector_1, vector_2):
        return Vector(vector_1.x - vector_2.x, vector_1.y - vector_2.y)

    def sub_(self, x, y, vector_2):
        self.x = x
        self.y = y
        v = Vector(self.x - vector_2.x, self.y - vector_2.y)
        return v.x, v.y
