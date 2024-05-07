import mlflow
from mlflow_extra.loggers.utils import check_metric
from mlflow_extra.loggers.utils import check_metrics
from mlflow_extra.loggers.utils import check_param
from mlflow_extra.loggers.utils import check_params


def metric(func):

    def wrapper(*args, **kwargs):
        run = mlflow.active_run()
        if run is None:
            raise mlflow.exceptions.MlflowException("No active run found.")

        result = func(*args, **kwargs)

        if check_metrics(result):
            mlflow.log_metrics(result)

        elif check_metric(result):
            mlflow.log_metric(key=result[0], value=result[1])
        else:
            raise Exception("Invalid metric format.")

    return wrapper


def param(func):

    def wrapper(*args, **kwargs):
        run = mlflow.active_run()
        if run is None:
            raise mlflow.exceptions.MlflowException("No active run found.")

        result = func(*args, **kwargs)

        if check_params(result):
            mlflow.log_params(result)

        elif check_param(result):
            mlflow.log_param(key=result[0], value=result[1])
        else:
            raise Exception("Invalid param format.")

    return wrapper
