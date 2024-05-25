from ml_extra.loggers.decorators.utils import check_run
from ml_extra.loggers.decorators.utils import get_valid_artifact_path_for_modules

from functools import wraps


import mlflow


def log_figures(func):
    """
    Log the figures returned by the decorated function.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        if not check_run():
            return func(*args, **kwargs)

        result = func(*args, **kwargs)

        for name, fig in result.items():
            mlflow.log_figure(fig, name)

        return result

    return wrapper
