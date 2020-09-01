def sequence():
    squared = []
    for i in range(10):
        squared.append(i**2)
    return squared


lc_sequence = [i**2 for i in range(10)]


def generator_sequence():
    for i in range(10):
        yield i**2


gc_sequence = (i**2 for i in range(10))
