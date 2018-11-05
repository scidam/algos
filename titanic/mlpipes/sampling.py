
from collections.abc import Iterable
from .pfunc import check_type
import numpy as np

@check_type()
def sample_like_target(target, source, grouping=None, using=None, ratio_using=0.6, train_test_ratio=0.8, n_choices=3,
                       balanced=False, n_clusters=None, filter_target_outliers=False):
    if n_clusters is not None:
        pass # Do clastering here!

    common_features = set(target.columns.tolist()).intersection(source.columns.tolist())

    if using is not None:
        common_features = list(common_features.intersection(set(using)))

    # clear outliers first
    size = int(ratio_using * source.shape[0])
    train_size = int(size * train_test_ratio)
    test_size = size - train_size

    if target.shape[0] <= (size / n_choices):
        raise Exception("Not enough target data, decrease ratio or increase n_choices parameters.")

    selected_target = target.loc[:, common_features].dropna().iloc[np.random.choice(size, replace=False), :]
    target_test = selected_target[:test_size]
    target_train = selected_target[test_size:]
    




