import logging


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('FlappyPy')

# this is the initial module of the app
# this is executed whenever some client-code is calling `import FlappyPy` or `from FlappyPy import ...`
# put the main classes here:
class MyClass:
    def my_method(self):
        return "Hello buddy! You will play FlappyPy soon!"


# let this be the last line of this file
logger.info("FlappyPy loaded")