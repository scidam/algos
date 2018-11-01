import pytest
import numpy as np
import pandas as pd
from ..preprocessing import (DropColumns,)

def test_drop_colums_typechecking():
    dc = DropColumns(colnames=['x', 'y'])
    with pytest.raises(Exception) as exinfo:
        dc.transform(dict())
    assert 'First argument' in str(exinfo.value)

def test_drop_columns_work():
    df = pd.DataFrame({'x': [1, 2, 3], 'y': [2, 3, 4], 'z': [6, 7, 8]})
    colnames = ['a', 'b', 'y', 'z']
    print("Here am I ")
    dc = DropColumns(colnames=colnames)
    assert ['x'] == dc.fit_transform(df).columns.tolist()

