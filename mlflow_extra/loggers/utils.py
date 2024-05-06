from typing import Tuple 
from typing import Dict 

def check_metrics(metrics:Dict[str, float])->bool:
    """
    Check if the metrics are a dictionary with string keys and int/float values.

    :param metrics: The metrics to check.
    :return: True if the metrics are a dictionary with string keys and int/float values, False otherwise.
    """
    if isinstance(metrics, dict) and all(isinstance(k, str) for k in metrics.keys()):
        return True
    return False

def check_metric(metric:Tuple)->bool:
    """
    Check if the metric is a tuple with a string key and an int/float value.

    :param metric: The metric to check.
    :return: True if the metric is a tuple with a string key and an int/float value, False otherwise.
    """
    if (
        isinstance(metric, tuple)
        and len(metric) == 2
        and isinstance(metric[0], str)
        and isinstance(metric[1], (int, float))
    ):
        return True
    return False

def check_params(params:Dict[str, str])->bool:
    """
    Check if the params are a dictionary with string keys and string values.

    :param params: The params to check.
    :return: True if the params are a dictionary with string keys and string values, False otherwise.
    """
    if isinstance(params, dict) and all(isinstance(k, str) for k in params.keys()):
        return True
    return False

def check_param(param:Tuple)->bool:
    """
    Check if the param is a tuple with a string key and a string value.

    :param param: The param to check.
    :return: True if the param is a tuple with a string key and a string value, False otherwise.
    """
    if (
        isinstance(param, tuple)
        and len(param) == 2
        and isinstance(param[0], str)
        and isinstance(param[1], str)
    ):
        return True
    return False