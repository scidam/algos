import re
import pandas as pd

cabin_letter_pat = re.compile(r'([a-zA-Z]+)d+')

def parse_name(s):
    a, b = s.split(',')
    family_name = a.strip()
    title = b.split('.')[0].strip()
    first_name = b.split('.')[1].split()[0].strip()
    return (first_name.replace('(', '').replace(')', ''), title, family_name)



def get_family_size(df):
    df_ = df.copy()
    df_.loc[:, 'family_size'] = df.Parch + df.SibSp + 1
    return df_

def get_cabin_letter(df):
    df_ = df.copy()
    df_.loc[~pd.isnull(df.Cabin), 'Cabin'] = df.loc[~pd.isnull(df.Cabin), 'Cabin'].apply(lambda x: x.strip()[0])
    df_.loc[pd.isnull(df.Cabin), 'Cabin'] = '0'
    df_.loc[~pd.isnull(df.Cabin), 'Cabin_nan'] = 0
    df_.loc[pd.isnull(df.Cabin), 'Cabin_nan'] = 1
    return df_