
import pytest
import pandas as pd
from ..pfunc import drop_columns



def test_type_checks():
    adict = dict(a=[1,2,3], b=4.5)
    with pytest.raises(Exception) as exinfo:
        drop_columns(adict, columns=('a',))
    assert 'First argument' in str(exinfo.value)

def test_dropcolumns():
    df = pd.DataFrame({'x': [1,2,3], 'y': [2,3,4], 'z': [6,7,8]})
    colnames = ['a', 'b', 'y', 'z']
    assert ['x'] == drop_columns(df, colnames=colnames).columns.tolist()






