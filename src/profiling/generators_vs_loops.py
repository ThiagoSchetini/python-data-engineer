from generators.operations import SquareCreator
from loggers.default import SimpleLogger


class GeneratorProfiler:

    def __init__(self, multiplier):
        self.multiplier = multiplier
        self.sc = SquareCreator(multiplier)
        self.log = SimpleLogger().get()

    def run(self):
        self.log.info('starting loop_sequence')
        self.sc.loop_sequence()
        self.log.info('starting generator_sequence')
        self.sc.generator_sequence()
        self.log.info('starting list_comprehension_sequence')
        self.sc.list_comprehension_sequence()
        self.log.info('starting generator_comprehension_sequence')
        self.sc.generator_comprehension_sequence()


def main():
    profiler = GeneratorProfiler(100000000)  # TODO get multiplier from a config file
    profiler.run()


if __name__ == '__main__':
    main()
