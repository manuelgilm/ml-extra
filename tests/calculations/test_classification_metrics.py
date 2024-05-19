from ml_extra.calculations.classification_metrics import get_classification_metrics


def test_output_type():
    y_true = [0, 1, 1, 0, 1, 1]
    y_pred = [0, 0, 1, 0, 1, 1]
    metrics = get_classification_metrics(y_true, y_pred)
    assert isinstance(metrics, dict)

def test_output_keys():
    y_true = [0, 1, 1, 0, 1, 1]
    y_pred = [0, 0, 1, 0, 1, 1]
    metrics = get_classification_metrics(y_true, y_pred)
    assert set(metrics.keys()) == set([
        "metrics_accuracy",
        "metrics_precision",
        "metrics_recall",
        "metrics_f1",
        "metrics_roc_auc",
        "metrics_confusion_matrix"
    ])