import inspect
import mlflow 

from typing import Optional

def log_code(name:Optional[str]=None):
    """Log the code of the function passed as argument."""
    
    if name.split(".")[-1] != "py" and name is not None:
        name += ".py"

    def inner(func):
        """Log the code of the function passed as argument."""
        def wrapper(*args, **kwargs):
            run = mlflow.active_run()
            if run is None:
                raise mlflow.exceptions.MlflowException("No active run found.")
            code = inspect.getsource(func)
            if name is not None:
                mlflow.log_text(code, name)
            else:
                mlflow.log_text(code, func.__name__ + ".py")

        return wrapper
    return inner


def log_code_path(func):
    """Log the code of the function passed as argument."""
    def wrapper(*args, **kwargs):
        run = mlflow.active_run()
        if run is None:
            raise mlflow.exceptions.MlflowException("No active run found.")
        
        code = inspect.getsource(func)
        module_name = func.__module__
        mlflow.log_text(code, module_name.replace(".","/") + ".py")

    return wrapper

def log_class(cls):

    orig_init = cls.__init__

    def __init__(self, *args, **kws):
        run = mlflow.active_run()
        if run is None:
            raise mlflow.exceptions.MlflowException("No active run found.")
        
        code = inspect.getsource(cls)
        module_name = cls.__module__
        mlflow.log_text(code, module_name.replace(".","/") + ".py")
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
        mlflow.log_text(code, module_name.replace(".","/") + ".py")
        return func(self, *args, **kwargs)

    return wrapper