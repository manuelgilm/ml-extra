from mlflow_extra.experiments.utils import get_or_create_experiment
from mlflow_extra.loggers.metrics import metric
from mlflow_extra.loggers.code import log_code
from mlflow_extra.tests.testing_functions import do_something
from mlflow_extra.tests.testing_functions import do_something_else
from mlflow_extra.tests.inner_test.dummy_module import do_something as ds
from mlflow_extra.tests.inner_test.dummy_module import dummy_function
from mlflow_extra.tests.testing_classes import DummyClass
from mlflow_extra.tests.testing_classes import DummyClass2
from mlflow_extra.tests.inner_test.dummy_module import AnotherClass
import mlflow

import inspect

import time


@metric
def calculate_metrics():
    return "custom_metric", 1.0


@log_code("promtps/custom_prompt.py")
def testing_function(a: int, b: int):
    result = a + b
    return result


def main():
    experiment = get_or_create_experiment(name="example_experiment")

    # str1 = inspect.getsource(get_or_create_experiment)
    # str2 = inspect.getsource(log_code)
    # total = "\n \n".join([str1,str2])

    # print(total)
    # print(type(inspect.getsource(get_or_create_experiment)))
    with mlflow.start_run(experiment_id=experiment.experiment_id):
        my_class = DummyClass()
        my_class.say_something("Hello")

        my_class2 = DummyClass2()
        my_class2.say_something("Hello")

        another_class = AnotherClass()
        another_class.say_something("Hello")
        calculate_metrics()
        testing_function(1, 2)
        do_something()
        do_something_else()
        ds()
        dummy_function()
