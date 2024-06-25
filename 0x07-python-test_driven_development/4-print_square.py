"""
module for printing square of #
"""


def print_square(size):
    """
    print square of #.
    arg:
        size: size of square.
    return:
        nothing.
    """
    if not isinstance(size, int):
        raise TypeError(
                'size must be an integer'
                )
    if size < 0:
        raise ValueError(
                'size must be >= 0'
                )
    if isinstance(size, float) and size < 0:
        raise TypeError(
                'size must be an integer'
                )
    for i in range (0, size):
        for j in range (0, size):
            print('#', end="")
        print("")
