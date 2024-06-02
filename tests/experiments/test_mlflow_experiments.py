from mlflow.entities import Experiment
def test_experiment_name(mlflow_experiment):
    assert mlflow_experiment.name == "TEST-EXPERIMENT"
    assert mlflow_experiment.lifecycle_stage == "active"
    assert isinstance(mlflow_experiment, Experiment)