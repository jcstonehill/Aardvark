import numpy as np

# https://codereview.stackexchange.com/questions/77593/calculating-the-volume-of-a-tetrahedron
def TetrahedronVolume(vertices=None, sides=None):
    """
    Return the volume of the tetrahedron with given vertices or sides. If
    vertices are given they must be in a NumPy array with shape (4,3): the
    position vectors of the 4 vertices in 3 dimensions; if the six sides are
    given, they must be an array of length 6. If both are given, the sides
    will be used in the calculation.

    Raises a ValueError if the vertices do not form a tetrahedron (for example,
    because they are coplanar, colinear or coincident). This method implements
    Tartaglia's formula using the Cayley-Menger determinant:
              |0   1    1    1    1  |
              |1   0   s1^2 s2^2 s3^2|
    288 V^2 = |1  s1^2  0   s4^2 s5^2|
              |1  s2^2 s4^2  0   s6^2|
              |1  s3^2 s5^2 s6^2  0  |
    where s1, s2, ..., s6 are the tetrahedron side lengths.

    Warning: this algorithm has not been tested for numerical stability.

    """

    # The indexes of rows in the vertices array corresponding to all
    # possible pairs of vertices
    vertex_pair_indexes = np.array(((0, 1), (0, 2), (0, 3),
                                    (1, 2), (1, 3), (2, 3)))
    if sides is None:
        # If no sides were provided, work them out from the vertices
        if type(vertices) != np.ndarray or vertices.shape != (4,3):
            raise TypeError('Invalid vertex array in tetrahedron_volume():'
                             ' vertices must be a numpy array with shape (4,3)')
        # Get all the squares of all side lengths from the differences between
        # the 6 different pairs of vertex positions
        vertex1, vertex2 = vertex_pair_indexes[:,0], vertex_pair_indexes[:,1]
        sides_squared = np.sum((vertices[vertex1] - vertices[vertex2])**2,
                               axis=-1)
    else:
        # Check that sides has been provided as a valid array and square it
        if type(sides) != np.ndarray or sides.shape != (6,):
            raise TypeError('Invalid argument to tetrahedron_volume():'
                             ' sides must be a numpy array with shape (6,)')
        sides_squared = sides**2

    # Set up the Cayley-Menger determinant
    M = np.zeros((5,5))
    # Fill in the upper triangle of the matrix
    M[0,1:] = 1
    # The squared-side length elements can be indexed using the vertex
    # pair indices (compare with the determinant illustrated above)
    M[tuple(zip(*(vertex_pair_indexes + 1)))] = sides_squared

    # The matrix is symmetric, so we can fill in the lower triangle by
    # adding the transpose
    M = M + M.T

    # Calculate the determinant and check it is positive (negative or zero
    # values indicate the vertices to not form a tetrahedron).
    det = np.linalg.det(M)
    if det <= 0:
        raise ValueError('Provided vertices do not form a tetrahedron')
    return np.sqrt(det / 288)


# intersection function
def IntersectionOfLineAndPlane(p0, p1, p_co, p_no, epsilon=1e-6):
    """
    p0, p1: Define the line.
    p_co, p_no: define the plane:
        p_co Is a point on the plane (plane coordinate).
        p_no Is a normal vector defining the plane direction;
             (does not need to be normalized).

    Return a Vector or None (when the intersection can't be found).
    """

    u = sub_v3v3(p1, p0)
    dot = dot_v3v3(p_no, u)

    if abs(dot) > epsilon:
        # The factor of the point between p0 -> p1 (0 - 1)
        # if 'fac' is between (0 - 1) the point intersects with the segment.
        # Otherwise:
        #  < 0.0: behind p0.
        #  > 1.0: infront of p1.
        w = sub_v3v3(p0, p_co)
        fac = -dot_v3v3(p_no, w) / dot

        if(fac > 1 or fac < 0):
            return None
            
        u = mul_v3_fl(u, fac)
        return add_v3v3(p0, u)

    # The segment is parallel to plane.
    return None

# ----------------------
# generic math functions

def add_v3v3(v0, v1):
    return (
        v0[0] + v1[0],
        v0[1] + v1[1],
        v0[2] + v1[2],
    )


def sub_v3v3(v0, v1):
    return (
        v0[0] - v1[0],
        v0[1] - v1[1],
        v0[2] - v1[2],
    )


def dot_v3v3(v0, v1):
    return (
        (v0[0] * v1[0]) +
        (v0[1] * v1[1]) +
        (v0[2] * v1[2])
    )


def len_squared_v3(v0):
    return dot_v3v3(v0, v0)


def mul_v3_fl(v0, f):
    return (
        v0[0] * f,
        v0[1] * f,
        v0[2] * f,
    )