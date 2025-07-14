import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('FlappyPy')

class MyClass:
    def my_method(self):
        return "Hello buddy! You will play FlappyPy soon!"


# let this be the last line of this file
logger.info("FlappyPy loaded")