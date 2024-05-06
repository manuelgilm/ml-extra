from mlflow_extra.loggers.code import log_method
from mlflow_extra.loggers.code import log_class

from abc import ABC 

@log_class
class DummyClass(ABC):

    def __init__(self):
        pass 

    @log_method
    def say_something(self, something):
        print(something)
