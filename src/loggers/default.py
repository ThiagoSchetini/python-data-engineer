import logging


class SimpleLogger:
    fmt = '[%(levelname)s] %(asctime)s %(name)s: %(message)s'
    lv = logging.INFO  # TODO get log level from config file
    simple_logger = logging

    def __init__(self):
        logging.basicConfig(level=self.lv, format=self.fmt)

    def get(self):
        return self.simple_logger
