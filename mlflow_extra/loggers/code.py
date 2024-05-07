import inspect
import mlflow

from typing import Optional
import tempfile
from pathlib import Path


def log_code(name: Optional[str] = None):
    """Log the code of the function passed as argument."""

    if name.split(".")[-1] != "py" and name is not None:
        name += ".py"
    
    def inner(func):
        """Log the code of the function passed as argument."""
        if name is None:
            name = func.__name__ + ".py"

        def wrapper(*args, **kwargs):
            run = mlflow.active_run()
            if run is None:
                raise mlflow.exceptions.MlflowException("No active run found.")
            
            code = inspect.getsource(func)
            mlflow.log_text(code, name)

        return wrapper

    return inner


def log_code_path(func):
    """Log the code of the function passed as argument."""

    def wrapper(*args, **kwargs):
        run = mlflow.active_run()
        if run is None:
            raise mlflow.exceptions.MlflowException("No active run found.")

        if check_logged_code(run, func):
            code = append_code(run, func)
        else:
            code = inspect.getsource(func)

        module_name = func.__module__
        mlflow.log_text(code, module_name.replace(".", "/") + ".py")

    return wrapper

def log_class(cls):

    orig_init = cls.__init__

    def __init__(self, *args, **kws):
        run = mlflow.active_run()
        if run is None:
            raise mlflow.exceptions.MlflowException("No active run found.")

        if check_logged_code(run, cls):
            code = append_code(run, cls)
        else:
            code = inspect.getsource(cls)

        module_name = cls.__module__
        mlflow.log_text(code, module_name.replace(".", "/") + ".py")

        # code = inspect.getsource(cls)
        # module_name = cls.__module__
        # mlflow.log_text(code, module_name.replace(".", "/") + ".py")
        orig_init(self, *args, **kws)

    cls.__init__ = __init__

    return cls


def log_method(func):
    def wrapper(self, *args, **kwargs):
        run = mlflow.active_run()
        if run is None:
            raise mlflow.exceptions.MlflowException("No active run found.")

        code = inspect.getsource(func)
        module_name = func.__module__
        mlflow.log_text(code, module_name.replace(".", "/") + ".py")
        return func(self, *args, **kwargs)

    return wrapper



def check_logged_code(run, func) -> bool:
    """
    Check if the code of the function has already been logged.

    :param run: The active run.
    :param func: The function to check.
    :return: True if the code of the function has already been logged, False otherwise.
    """
    module_path = Path(func.__module__.replace(".", "/") + ".py")
    artifacts = mlflow.artifacts.list_artifacts(
        run_id=run.info.run_id, artifact_path=module_path.parent
    )
    if artifacts:
        files = [file.path for file in artifacts]
        if module_path.as_posix() in files:
            return True
    else:
        return False


def append_code(run, func) -> str:
    """
    Append the code of the function to the code of the module.

    :param run: The active run.
    :param func: The function to append.
    :return: The full code of the module.
    """
    module_name = func.__module__
    with tempfile.TemporaryDirectory() as tmpdirname:
        mlflow.artifacts.download_artifacts(
            run_id=run.info.run_id,
            artifact_path=module_name.replace(".", "/") + ".py",
            dst_path=tmpdirname,
        )
        with open(tmpdirname + "/" + module_name.replace(".", "/") + ".py", "r") as f:
            code = f.read()
            func_code = inspect.getsource(func)
            full_code = "\n\n".join([code, func_code])
    return full_code

