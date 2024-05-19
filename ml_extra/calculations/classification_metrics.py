from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import roc_auc_score
from sklearn.metrics import confusion_matrix

from sklearn.metrics import RocCurveDisplay
from sklearn.metrics import PrecisionRecallDisplay
from sklearn.metrics import ConfusionMatrixDisplay

import matplotlib.pyplot as plt 

from typing import Optional
from typing import Dict
from typing import Union
from typing import Tuple

import pandas as pd
import numpy as np


def get_classification_metrics(
    y_true: Union[pd.Series, np.ndarray],
    y_pred: Union[pd.Series, np.ndarray],
    prefix: Optional[str] = "metrics",
) -> Dict[str, float]:
    """
    Get classification metrics for a binary classification problem.

    :param y_true: True labels.
    :param y_pred: Predicted labels.
    :param prefix: Prefix for the metric names.
    :return: Dictionary with the metrics.
    """
    metrics = {}
    metrics[prefix + "_accuracy"] = accuracy_score(y_true, y_pred)
    metrics[prefix + "_precision"] = precision_score(y_true, y_pred)
    metrics[prefix + "_recall"] = recall_score(y_true, y_pred)
    metrics[prefix + "_f1"] = f1_score(y_true, y_pred)
    metrics[prefix + "_roc_auc"] = roc_auc_score(y_true, y_pred)
    metrics[prefix + "_confusion_matrix"] = confusion_matrix(y_true, y_pred)

    return metrics


def get_figure_performance(
    y_true: Union[pd.Series, np.ndarray],
    y_pred: Union[pd.Series, np.ndarray],
    name: Optional[str] = "Classifier",
    prefix: Optional[str] = "metrics",
    figsize: Optional[Tuple] = (15, 5),
):
    """
    Get the performance figure.

    :param y_true: True labels.
    :param y_pred: Predicted labels.
    :param prefix: Prefix for the metric names.
    :return: The performance figure.
    """
    
    plt.figure(figsize=figsize)
    roc_display = RocCurveDisplay.from_predictions(y_true, y_pred, name=name, ax=plt.gca())

    plt.figure(figsize=figsize)
    pr_display = PrecisionRecallDisplay.from_predictions(y_true, y_pred, name=name, ax=plt.gca())

    return {
        f"{prefix}_roc_display": roc_display.figure_,
        f"{prefix}_pr_display": pr_display.figure_,
    }
    
