import itertools
from functools import wraps
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from collections.abc import Iterable, Callable

__all__ = ('drop_columns', 'get_ohe', 'get_le',
           'merge_categories', 'fill_na_simple')


def check_type(itype=pd.DataFrame):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not isinstance(args[0], itype):
                raise(Exception("First argument should be an instance of {}".format(itype)))
            return func(*args, **kwargs)
        return wrapper
    return decorator


def filter_colnames(df, colnames=None):
    print("Colnames ", colnames)
    if isinstance(colnames, Iterable):
        print("I am here", colnames)
        return [col for col in colnames if col in df.columns]
    return list()


@check_type()
def drop_columns(df, colnames=tuple()):
    """Drops specified columns from a DataFrame"""
    return df.drop(filter_colnames(df, colnames), axis=1)


@check_type()
def get_ohe(df, colnames=tuple(), prefix=None, drop=True):
    """Encodes specified df-columns in one-hot fashion"""
    colnames = filter_colnames(df, colnames)
    auxiliary_df = pd.get_dummies(df.loc[:, colnames], prefix=prefix, columns=colnames)
    if drop:
        return pd.concat([df.drop(colnames, axis=1), auxiliary_df], axis=1)
    else:
        return pd.concat([df, auxiliary_df], axis=1)

@check_type()
def get_le(df, colnames=tuple(), prefix=None, drop=True):

    sep = '_'

    colnames = filter_colnames(df, colnames)

    if not colnames:
        return df

    enc = LabelEncoder()
    labels = dict()
    result_df = pd.DataFrame()
    if prefix is None or not isinstance(prefix, str):
        prefix = 'LE'

    for col in colnames:
        encoded = enc.fit_transform(df.loc[:, col].values)
        result_df[:, prefix + sep + col] = encoded
        labels[col] = enc.classes_

    if drop:
        return (pd.concat([df.drop(colnames, axis=1), result_df], axis=1), labels)
    else:
        return (pd.concat([df, result_df], axis=1), labels)

@check_type()
def merge_categories(df, colnames=tuple(), mapping=dict()):
    """

    Usage
    -----
    """
    colnames = filter_colnames(df, colnames)

    if not colnames or not mapping:
        return df

    if (set(df.colnames) - set(mapping.keys())):
        # check if mapping keys doesn't cover all colnames
        raise Exception("Mapping argument should cover all specified column names")

    _df = df.copy()
    for col in colnames:
        mask = df.loc[:, col].isin(mapping[col]['what'])
        _df.loc[:, col][mask] = mapping[col]['to']

    return _df, mapping

@check_type()
def fill_na_simple(df, colnames=tuple(), methods=tuple()):

    if isinstance(methods, Iterable):
        if len(colnames)!= len(methods):
            raise Exception('Colnames and methods arrays should have the same length')
    elif isinstance(methods, Callable):
        methods = (methods, )
    else:
        methods = (pd.np.median, )

    colnames = filter_colnames(df, colnames)

    if len(methods) > len(colnames):
        zipped = zip(colnames, itertools.cycle(methods))
    else:
        zipped = zip(itertools.cycle(colnames), methods)

    res_df = df.copy()
    for col, met in zipped:
        if isinstance(met, Callable):
            method = met
        value = method(res_df.loc[:, col].dropna().values)
        res_df.loc[:, col].fillna(value, inplace=True)
    return res_df






