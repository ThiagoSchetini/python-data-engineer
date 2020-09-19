import timeit
from generators.operations import SquareCreator

sc = SquareCreator(1000)

sc.loop_sequence()
#timeit.timeit(sc.loop_sequence())
#timeit.timeit(sc.generator_sequence())
#timeit.timeit(sc.list_comprehension_sequence())
#timeit.timeit(sc.generator_comprehension_sequence())
