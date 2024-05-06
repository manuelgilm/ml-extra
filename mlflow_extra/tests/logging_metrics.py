from mlflow_extra.experiments.utils import get_or_create_experiment
from mlflow_extra.loggers.metrics import metric
from mlflow_extra.loggers.code import log_code
from mlflow_extra.tests.testing_functions import do_something
from mlflow_extra.tests.testing_classes import DummyClass
import mlflow


@metric
def calculate_metrics():
    return "custom_metric", 1.0

@log_code("promtps/custom_prompt.py")
def testing_function(a:int, b:int):
    result = a + b
    return result



def main():
    experiment = get_or_create_experiment(name="example_experiment")
    # print(inspect.stack()[0])
    # print(inspect.getsource(get_or_create_experiment))
    with mlflow.start_run(experiment_id=experiment.experiment_id):
        my_class = DummyClass()
        my_class.say_something("Hello")
        calculate_metrics()
        testing_function(1, 2)
        do_something()
