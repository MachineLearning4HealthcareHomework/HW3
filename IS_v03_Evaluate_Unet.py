import numpy as np
from sklearn import metrics

# ------------------------------
# Get scores
# ------------------------------
test_labels = np.load("labels_test.npy")
test_labels_pred = np.load("test_labels_pred.npy")
test_labels_pred = np.squeeze(test_labels_pred)

def get_scores(y_true, y_pred):
    results=[]
    y_true=y_true.flatten()
    y_pred=y_pred.flatten()
    #Overall precision
    results.append(metrics.precision_score(y_true, y_pred, average='micro'))
    #Per-class precision
    results.append(metrics.precision_score(y_true, y_pred, average='macro'))
    #jaccard (right average?)
    results.append(metrics.jaccard_score(y_true, y_pred, average='macro'))
    return results
get_scores(test_labels,test_labels_pred)
