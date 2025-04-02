# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(x: int, y: int) -> int:
    """
    Returns the result of summation of two numbers between 0 and 100

    Args :
    x : integer between 0 to 100
    y : integer between 0 to 100

    Returns: 
    An integer which is summation of x and y

    Raise ValueError if arguments are outside the range [0,100]
    """
    if x < 0 or x > 100:
        raise ValueError("x must be between 0 and 100")

    if y < 0 or y > 100:
        raise ValueError("y must be between 0 and 100")

    return x + y
