class SquareCreator:

    def __init__(self, multiplier):
        self.multiplier = multiplier

    def loop_sequence(self):
        squared = []
        for i in range(self.multiplier):
            squared.append(i ** 2)
        return squared

    def generator_sequence(self):
        for i in range(self.multiplier):
            yield i ** 2

    def list_comprehension_sequence(self):
        return [i ** 2 for i in range(self.multiplier)]

    def generator_comprehension_sequence(self):
        return (i ** 2 for i in range(self.multiplier))
