# Vectors
An implementation of vectors in 2 and 3-dimensional euclidean space.

A ```Vector``` object can be created by assigning it either two or three components, for a two or a three-dimensional vector, respectively.

```python
v = new Vector(1, 2)     # => <1, 2>
v = new Vector(1, 2, 3)  # => <1, 2, 3>
```

All the standard vector operations are available:
- ```vector.mag()```  -  Returns the magnitude of the vector.
- ```vector.scalar(a)``` - Multiples the vector by a scalar *a*.
