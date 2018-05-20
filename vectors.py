#
# vectors.py - implementation of vectors in 2 and 3-dimensional euclidean space
#

import math
import types

# needs support for a + b, c*a
class Vector:

    def __init__(self, x1, x2, x3=0):

        # instance variables
        self.x = x1
        self.y = x2
        self.z = x3

    # returns a string representation of the vector
    @property
    def display(self):
        # displays differently if vector is 2D or 3D
        if (self.z == 0):
            return "<{}, {}>".format(self.x, self.y)
        else:
            return "<{}, {}, {}>".format(self.x, self.y, self.z)

    # vector addition
    def __add__(self, other):
        return Vector((self.x + other.x), (self.y + other.y), (self.z + other.z));

    # vector subtraction
    def __sub__(self, other):
        return Vector((self.x - other.x), (self.y - other.y), (self.z - other.z));


    # returns the magnitude of the vector
    @property
    def mag(self):
       return math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2) + math.pow(self.z, 2))


    # returns a new vector multiplied by the scalar m
    def scalar(self, m):
        return Vector(self.x * m, self.y * m, self.z * m)

    # returns the normalization of the vector
    @property
    def norm(self):
        return Vector((self.x/self.mag), (self.y/self.mag), (self.z/self.mag))


    # returns a scalar, the dot product with a given vector
    def dot(self, vector):
        return (self.x * vector.x) + (self.y * vector.y) + (self.z * vector.z)


    # angle between two vectors
    def theta(self, vector):
        return math.acos((self.dot(vector)) / (self.mag * vector.mag));


    # cross product
    def cross(self, vector):
        x = (self.y * vector.z) - (self.z * vector.y)
        y = (self.z * vector.x) - (self.x * vector.z)
        z = (self.x * vector.y) - (self.y * vector.x)
        return Vector(x, y, z)


    # scalar projection onto a given vector
    def comp(self, vector):
        return self.dot(vector.norm)


    # vector projection onto a given vector
    def proj(self, vector):
        return vector.norm.scalar(self.dot(vector.norm))

    # defines the '*' operator to give either the scalar multiplication or the cross product
    def __mul__(self, other):

        if (isinstance(other, types.IntType)):
           return self.scalar(other)
        if (isinstance(other, Vector)):
           return self.cross(other)


    def __rmul__(self, other):
        return self.scalar(other)
