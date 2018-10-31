
from sklearn.base import BaseEstimator, TransformerMixin
from .pfunc import (drop_columns, get_ohe, get_le, merge_categories,
                    fill_na_simple)
import pandas as pd


class AbstractPreprocessor(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        if not isinstance(X, pd.DataFrame):
            raise Exception("Input data should be a DataFrame instance")
        return self



# Probably it is better to create metaclass that do all the work!!! func -> pipeline model


class DropColumns(AbstractPreprocessor):
    '''
    Drops specified columns from a DataFrame.

    Input data assumed to be a DataFrame.

    Usage
    -----
            # TODO: upgrade needed!!!
        dropper = DropColumns(names=['PassengerId', 'Ticket'])
        dropped_df = dropper.fit_transform(source_dataframe)
    '''

    def __init__(self, colnames=[]):
        self.colnames = colnames

    def transform(self, X, y=None):
        return drop_columns(X, colnames=self.colnames)


class OneHotEncodeAndDrop(AbstractPreprocessor):

    def __init__(self, colnames=None, prefix=None):
        self.colnames = colnames
        self.prefix = prefix

    def transform(self, X, y=None):
        return get_ohe(X, prefix=self.prefix)


class LabelEncodeAndDrop(AbstractPreprocessor):

    def __init__(self, colnames=None, prefix=None, drop=True):
        self.colnames = colnames
        self.prefix = prefix
        self.drop = drop

    def transform(self, X, y=None):
        res, classes_ = get_le(X, columns=self.colnames, prefix=self.prefix,
                               drop=self.drop)
        self.classes_ = classes_
        return res


class MergeCategories(AbstractPreprocessor):
    def __init__(self, colnames=None, mapping=dict()):
        self.colnames = colnames
        self.mapping = mapping

    def transform(self, X, y=None):
        res, mapping = merge_categories(X, colnames=self.colnames,
                                        mapping=self.mapping)
        self.mapping_ = mapping
        return res


class FillNaSimple(AbstractPreprocessor):
    def __init__(self, colnames=tuple(), methods=tuple()):
        self.colnames = colnames
        self.methods = methods

    def transform(self, X, y=None):
        return fill_na_simple(X, colnames=self.colnames, methods=self.methods)
