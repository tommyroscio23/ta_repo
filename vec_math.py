def _validate_3d_vector(vec: list | tuple) -> bool:
    """
    Confirms that variable is a 3d numerical vector.
    """

    if len(vec) != 3:
        raise ValueError(f"The vector {vec} is not a 3d vector.")
    if not all(isinstance(x, (float, int)) for x in vec):
        raise TypeError(f"{vec} contains non-number elements.")
    return True


def add_3d_vectors(vec_1: list | tuple, vec_2: list | tuple) -> list:
    """
    Returns the sum of two 3d vectors.
    """

    for vec in (vec_1, vec_2):
        _validate_3d_vector(vec)
    return [x + y for x, y in zip(vec_1, vec_2)]


def subtract_3d_vectors(vec_1: list | tuple, vec_2: list | tuple) -> list:
    """
    Returns the substraction of two 3d vectors.
    """
    for vec in (vec_1, vec_2):
        _validate_3d_vector(vec)
    return [x - y for x, y in zip(vec_1, vec_2)]


def scale_3d_vector(vec: list | tuple, scalar: float | int) -> list:
    """
    Multiplies 3d vector by a scalar.
    """
    _validate_3d_vector(vec)
    if not isinstance(scalar, (float, int)):
        raise TypeError(f"{scalar} is not a number.")
    return [x * scalar for x in vec]


def get_3d_vector_magnitude(vec: list | tuple) -> float:
    """
    Returns the magnitude of a 3d vector.
    """
    _validate_3d_vector(vec)
    return sum(x**2 for x in vec) ** 0.5


def normalize_3d_vector(vec: list | tuple) -> list:
    """
    Normalizes a 3d vector.
    """
    vec_magnitude = get_3d_vector_magnitude(vec)
    if vec_magnitude <= 1e-8:
        return [0, 0, 0]
    return [x / vec_magnitude for x in vec]


def get_3d_vector_dot_product(vec_1: list | tuple, vec_2: list | tuple) -> float:
    """
    Returns the dot product of two 3d vectors
    """
    for vec in (vec_1, vec_2):
        _validate_3d_vector(vec)
    return sum(x * y for x, y in zip(vec_1, vec_2))


def get_3d_vector_cross_product(vec_1: list | tuple, vec_2: list | tuple) -> list:
    """
    Returns the cross product of two 3d vectors
    """
    for vec in (vec_1, vec_2):
        _validate_3d_vector(vec)
    x = vec_1[1] * vec_2[2] - vec_1[2] * vec_2[1]
    y = vec_1[2] * vec_2[0] - vec_1[0] * vec_2[2]
    z = vec_1[0] * vec_2[1] - vec_1[1] * vec_2[0]
    return [x, y, z]


if __name__ == "__main__":

    vec_1 = [1, 2, 3]
    vec_2 = [4, 5, 6]
    vec_3 = [10, 0, 0]
    vec_4 = [5, 10, 10]
    scalar = 10
    print(add_3d_vectors(vec_1, vec_2))
    print(subtract_3d_vectors(vec_1, vec_2))
    print(scale_3d_vector(vec_1, scalar))
    print(get_3d_vector_magnitude(vec_1))
    print(normalize_3d_vector(vec_1))
    print(get_3d_vector_dot_product(vec_3, vec_4))
    cross_product = get_3d_vector_cross_product(vec_1, vec_2)
    print(cross_product)
    print(get_3d_vector_dot_product(cross_product, vec_1))
