from .test_lib import *

__doc__ = test_lib.__doc__
if hasattr(test_lib, "__all__"):
    __all__ = test_lib.__all__


def hello():
    return "Hello, world!"
