from ml_extra.decorators.mlflow.exp_tracking import mlflow_experiment 
from ml_extra.decorators.mlflow.exp_tracking import mlflow_client
import mlflow 

@mlflow_experiment(name="TEST-EXPERIMENT")
def test_create_experiment():
    """
    Function checks if the experiment is created
    """
    mlflow_experiment = mlflow.get_experiment_by_name("TEST-EXPERIMENT")
    assert mlflow_experiment.name == "TEST-EXPERIMENT"


@mlflow_experiment(name="TEST-EXPERIMENT-TAGS", tags={"key": "value"})
def test_create_experiment_with_tags():
    """
    Function checks if the experiment is created with tags
    """
    mlflow_experiment = mlflow.get_experiment_by_name("TEST-EXPERIMENT-TAGS")
    assert mlflow_experiment.name == "TEST-EXPERIMENT-TAGS"
    assert mlflow_experiment.tags == {"key": "value"}


@mlflow_experiment(name="TEST-EXPERIMENT-RETURN-EXPERIMENT", tags={"key": "value"}, return_experiment=True)
def test_create_experiment_with_tags_and_return_experiment(**kwargs):
    """
    Function checks if the experiment is created with tags and returns the experiment object
    within the kwargs.
    """
    mlflow_experiment = kwargs.get("mlflow_experiment")
    assert mlflow_experiment.name == "TEST-EXPERIMENT-RETURN-EXPERIMENT"
    assert mlflow_experiment.tags == {"key": "value"}

@mlflow_experiment(name="TEST-EXPERIMENT-NO-EXPERIMENT", tags={"key": "value"}, return_experiment=False)
def test_create_experiment_with_tags_no_return_experiment(**kwargs):
    """
    Function checks if the experiment is created with client
    """
    mlflow_experiment = kwargs.get("mlflow_experiment", None)
    assert mlflow_experiment is None # client is not passed
    # check experiment is created
    mlflow_experiment = mlflow.get_experiment_by_name("TEST-EXPERIMENT-NO-EXPERIMENT")
    assert mlflow_experiment.name == "TEST-EXPERIMENT-NO-EXPERIMENT"

@mlflow_client
def test_create_experiment_with_client(**kwargs):
    """
    Function checks if the client is passed 
    """
    mlflow_client = kwargs.get("mlflow_client", None)
    assert mlflow_client is not None