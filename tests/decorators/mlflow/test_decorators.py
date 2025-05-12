from ml_extra.decorators.mlflow.exp_tracking import mlflow_experiment 
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
    