def _validate_3d_vector(vec: list | tuple):
    """
    Confirms that variable is a 3d numerical vector.
    """

    if len(vec) != 3:
        raise ValueError(f"The vector {vec} is not a 3d vector.")
    if not all(isinstance(x, (float, int)) for x in vec):
        raise TypeError(f"{vec} contains non-number elements.")
    return True


def add_3d_vectors(vec_1: list | tuple, vec_2: list | tuple):
    """
    Returns the sum of two 3d vectors
    """

    for vec in (vec_1, vec_2):
        _validate_3d_vector(vec)
    return [x + y for x, y in zip(vec_1, vec_2)]


def subtract_3d_vectors(vec_1: list | tuple, vec_2: list | tuple):
    """
    Returns the substraction of two 3d vectors
    """
    for vec in (vec_1, vec_2):
        _validate_3d_vector(vec)
    return [x - y for x, y in zip(vec_1, vec_2)]


def scale_3d_vector(vec: list | tuple, scalar: float | int):
    """
    Multiplies 3d vector by a scalar
    """
    _validate_3d_vector(vec)
    if not isinstance(scalar, (float, int)):
        raise TypeError(f"{scalar} is not a number.")
    return [x * scalar for x in vec]


if __name__ == "__main__":

    vec_1 = [1, 2, 3]
    vec_2 = [4, 5, 6]
    scalar = 10
    print(add_3d_vectors(vec_1, vec_2))
    print(subtract_3d_vectors(vec_1, vec_2))
    print(scale_3d_vector(vec_1, scalar))
