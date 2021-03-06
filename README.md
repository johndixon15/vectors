# Vectors
An implementation of vectors in 2 and 3-dimensional euclidean space.

## Basic Use

A ```Vector``` object can be created by assigning it either two or three components, for a two or a three-dimensional vector, respectively.

```python
v = new Vector(1, 2)     # => <1, 2>
v = new Vector(1, 2, 3)  # => <1, 2, 3>
```

All the standard vector operations are available:
- ```vector.comp(v)``` - Returns the scalar projection onto a given ```Vector v```.
- ```vector.cross(v)``` - Returns the cross product with a given ```Vector v```.
- ```vector.display``` - Returns a string of the vector.
- ```vector.dot(v)``` - Returns the dot product with a given ```Vector v```.
- ```vector.mag``` - Returns the magnitude of the vector.
- ```vector.norm``` - Returns the normalization of the vector.
- ```vector.proj(v)``` - Returns the vector projection onto a given ```Vector v```.
- ```vector.scalar(a)``` - Multiples the vector by the scalar ```a```.
- ```vector.theta(v)``` - Returns the angle made with a given ```Vector v```.

