from collections.abc import Iterable
from .pfunc import check_type
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

try:
    import imblearn
except ImportError:
    raise Exception("Sampling package depends on imbalanced-learning package."
                    "Install imbalanced-learning package first.")


@check_type()
def sample_like_target(target, source, using=None, autoencode=False,
                       scale=True, random_state=None, fillna=True):

    if isinstance(using, Iterable):
        using = list(set(using))
    else:
        using = list(set(target.columns).intersection(set(source.columns)))

    T = target.copy().loc[:, using]
    S = source.copy().loc[:, using]

    if fillna:
        T.fillna(T.median(), inplace=True)
        S.fillna(S.median(), inplace=True)
    else:
        dropped_mask = pd.isnull(S).sum(axis=1).astype(np.bool)
        S = S.iloc[~dropped_mask, :]
        T = T.dropna()

    if autoencode:
        C = pd.concat([T, S]).reset_index(drop=True)
        R = pd.get_dummies(C, dummy_na=True)
        T = R.iloc[:T.shape[0], :]
        S = R.iloc[T.shape[0]:, :]

    if scale:
        scaler = StandardScaler()
        scaler.fit(T)
        T = scaler.transform(T)
        S = scaler.transform(S)




    combined = pd.concat([T, S]).reset_index(drop=True)
    y = [0] * T.shape[0] + [1] * S.shape[0]

    tmklnk = imblearn.under_sampling.TomekLinks([1], random_state=random_state)
    tmklnk.fit_resample(combined, y)
    return S.iloc[tmklnk.sample_indices_, :]


