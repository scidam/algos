
import pandas as pd
train = pd.read_csv("./data/train.csv")
test = pd.read_csv("./data/test.csv")

combined = pd.concat([train, test]).reset_index(drop=True)



# self explanatory function, returns first name, title and the last name of a passenger
def parse_name(s): 
    a, b = s.split(',')
    family_name = a.strip()
    title = b.split('.')[0].strip()
    first_name = b.split('.')[1].split()[0].strip()
    return (first_name, title, family_name)


from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import FunctionTransformer, LabelEncoder
from IPython.core.display import display, HTML



class AddFirstNameColumn(AbstractPreprocessor):

    def transform(self, X, y=None):
        result = X.copy()
        result['first_name'] = X.loc[:, 'Name'].apply(lambda x: parse_name(x)[0].replace('(', '').replace(')', ''))
        return result

class AddFamilyNameColumn(AbstractPreprocessor):
    def transform(self, X, y=None):
        result = X.copy()
        result['family_name'] = X.loc[:, 'Name'].apply(lambda x: parse_name(x)[-1])
        return result
                
class AddTitleColumn(AbstractPreprocessor):

    def transform(self, X, y=None):
        result = X.copy()
        result['title'] = X.loc[:, 'Name'].apply(lambda x: parse_name(x)[1])
        return result   

class AddFamilySize(AbstractPreprocessor):
    def transform(self, X, y=None):
        _X = X.copy()
        _X['family_size'] = X['SibSp'] + X['Parch'] + 1
        return _X

class AddIsAlone(AbstractPreprocessor):
    def transform(self, X, y=None):
        _X = X.copy()
        _X['is_alone'] = 1
        _X.loc[_X.family_size > 1,'is_alone'] = 0
        return _X


class SelectFeatures(AbstractPreprocessor):
    
    def __init__(self, k, n):
        self.k = k
        self.n = n

    def transform(self, X, y=None):
        _ = [int(x) for x in bin(self.k)[2:]]
        _ = [0] * (self.n - len(_)) + _
        return X.iloc[:, [j for j in range(self.n) if _[j]]]
    
    

        
class DropByValue(AbstractPreprocessor):
    def __init__(self, name=None, value=None):
        self.name = name
        self.value = value
    
    def transform(self, X, y=None):
        return X[X.loc[:, self.name] != self.value]
    
class GetCategoriesAndDrop(AbstractPreprocessor):
    def __init__(self, name=None, bins=None):
        self.name = name
        self.bins = bins
    
    def transform(self, X, y=None):
        if self.bins is not None and hasattr(X, self.name):
            aux = pd.qcut(X.loc[:, self.name], q=self.bins, labels=False)
            _X = X.drop(self.name, axis=1)
            _X[self.name] = aux
            return _X
        else:
            return X
   
    
from sklearn.ensemble import RandomForestRegressor
class FillNaValues(AbstractPreprocessor):

    def __init__(self, name=None, train=None, n_features=None,
                 clf=RandomForestRegressor()):
        self.train = train
        self.name = name
        self.clf = clf
        self.n_features = n_features
    
    def transform(self, X, y=None):

        if self.name is None: 
            return X

        if X.loc[:, self.name].isnull().sum() == 0:
            return X
        
        _train = self.train.copy() if self.train is not None else X.copy()
        null_mask = _train[self.name].isnull()
        y = _train[self.name][~null_mask]
        _train = _train.drop(self.name, axis=1)
        
        n_features = int(pd.np.ceil(X.shape[1] * 0.3) or self.n_features)
        
        encoders = dict()
        for key in _train.columns.tolist():
            if not pd.np.issubdtype(_train[key].dtype, pd.np.number):
                _train.loc[_train[key].isnull(), key]  = 'N-a-N'
                le = LabelEncoder()
                _train[key] = le.fit_transform(_train[key])
                encoders[key] = le
            else:
                if any(_train[key].isnull()):
                    _train['%s_nan' % key] = 0.0
                    _train.loc[_train[key].isnull(), '%s_nan' % key] = 1.0
                    _train.loc[_train[key].isnull(), key] = _train.loc[~_train[key].isnull(), key].median()

        self.clf.fit(_train[~null_mask], y)
        
        # dropping features
        if hasattr(self.clf, 'feature_importances_'):
            # drop columns and retrain classifier
            indices = pd.np.argsort(self.clf.feature_importances_)[::-1]
            features_to_drop = _train.columns[indices].values.tolist()[n_features:]
            self.clf.fit(_train.drop(features_to_drop, axis=1)[~null_mask], y)
        else:
            features_to_drop = []
            
        _X = X.copy()
        for key in _train.columns:
            if key not in _X.columns:
                _X.loc[:, key] = 0.0
        _X = _X[_train.columns]
        for key in encoders.keys():
            if not pd.np.issubdtype(_X[key].dtype, pd.np.number):
                _X.loc[_X[key].isnull(), key]  = 'N-a-N'
                _X[key] = encoders[key].transform(_X[key])
            else:
                if any(_X[key].isnull()):
                    _X['%s_nan' % key] = 0.0
                    _X.loc[_X[key].isnull(), '%s_nan' % key] = 1.0
                    _X.loc[_X[key].isnull(), key] = X.loc[~_X[key].isnull(), key].median()
        
        na_replacements = self.clf.predict(_X.drop(features_to_drop, axis=1)[null_mask])
        result = X.copy()
        result.loc[null_mask, self.name] = na_replacements
        return result


class FillNaSimple(AbstractPreprocessor):
    def __init__(self, name):
        self.name = name
    
    def fit(self, X, y=None):
        return self
    
    def transform(self, X, y=None):
        _X = X.copy()
        if hasattr(_X, self.name):
            _X.loc[:, self.name] = _X.loc[:, self.name].fillna(_X.loc[:, self.name].dropna().mode()[0])
        return _X
    
class DropRows(AbstractPreprocessor):

    def __init__(self, condition=None):
        self.condition = condition #condition depends on (X, y) and 
        # returns boolean array of the same length as X

    def fit(self, X, y=None):
        return self
    
    def trasform(self, X, y=None):
        if self.condition is not None:
            return X[self.condition(X, y)]
        else:
            return X


class ShowDataHead(AbstractPreprocessor):
    def fit(self, X, y=None):
        display(HTML(X.head().to_html()))
        return self
        
    def transform(self, X, y=None):
        return X


# # Preprocessing steps (feature engeneering)

# In[16]:


from sklearn.pipeline import Pipeline
preprocessing_steps = [('drop_columns', DropColumns(names=['Ticket', 'PassengerId', 'Cabin', 'Survived'])),
                       ('add_title', AddTitleColumn()),
                       # ('add_first_name', AddFirstNameColumn()),
                       #('add_family_name', AddFamilyNameColumn()),
                       ('add_family_size', AddFamilySize()),
                       ('encode_sex', LabelEncodeAndDrop(name='Sex')),
                       ('fillna_embarked', FillNaSimple(name='Embarked')),
                       #('combine_embarked', CombineCategoricalValues(name='Embarked', rule={'what': ['C', 'Q'], 'to': 'Q'})),
                       ('encode_embarked', LabelEncodeAndDrop(name='Embarked')),
                       
                       # predicting nan-values
                       ('predict_fare', FillNaSimple(name='Fare')),
                       ('predict_age', FillNaSimple(name='Age')),
                    #  ('cat_ages', GetCategoriesAndDrop(name='Age', bins=[0, 0.3, 0.6, 1.0])),
                    #  ('cat_fares', GetCategoriesAndDrop(name='Fare', bins=[0, 0.3, 0.6, 1.0])),
                       
                       # combine & encode titles
                       #('combine_title_Mrs', CombineCategoricalValues(name='title', rule={'what': ['Dona', 'Mme', 'the Countess'], 'to': 'Mrs'})),
                       #('combine_title_Mr', CombineCategoricalValues(name='title', rule={'what': ['Jonkheer', 'Major', 'Col', 'Rev', 'Mr'], 'to': 'Mr1'})),
                       #('combine_title_Mr', CombineCategoricalValues(name='title', rule={'what': ['Master', 'Sir', 'Don', 'Dr'], 'to': 'Mr2'})),
                       #('combine_title_Miss', CombineCategoricalValues(name='title', rule={'what': ['Mlle','Lady','Ms'], 'to': 'Miss'})),
                       ('combine_title_rare', CombineCategoricalValues(name='title', rule={'what': ['Rev', 'Dr', 'Col', 'Ms', 'Mlle', 'Major', 'Sir', 'Mme','Lady','Capt','the Countess','Jonkheer','Don','Dona'], 'to': 'rare'})),
                       ('encode_title', LabelEncodeAndDrop(name='title')),
                       
                       #
                       #('add_is_alone', AddIsAlone()),
                       
                       # last one-hots... 
                       #('encode_fare', OneHotEncodeAndDrop(name='Fare')),
                       #('encode_age', OneHotEncodeAndDrop(name='Age')),
                       #('encode_Pclass', OneHotEncodeAndDrop(name='Pclass')),
                       #('combine_fsize', CombineCategoricalValues(name='family_size', rule={'what': ['5','6', '7','8','9','10','11'], 'to': '5'})),
                       #('encode_fsize', OneHotEncodeAndDrop(name='family_size')),
                       
                       #drop first name, family name
                       ('drop_last', DropColumns(names=['first_name','family_name', 'Name'])),
                       ('show_data', ShowDataHead())
                      ]

preprocessing_pipeline = Pipeline(steps=preprocessing_steps)
combined_processed = preprocessing_pipeline.fit_transform(combined)


# # It seems that all is ready. Lets make a classifier!

# In[8]:


from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, AdaBoostClassifier, VotingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import Perceptron
from sklearn.linear_model import SGDClassifier
from sklearn.tree import DecisionTreeClassifier, ExtraTreeClassifier
from sklearn.model_selection import cross_val_score, GridSearchCV
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis, QuadraticDiscriminantAnalysis
from sklearn.pipeline import make_pipeline


# In[9]:


train_processed = combined_processed.iloc[:train.shape[0]]
test_processed = combined_processed.iloc[train.shape[0]:]
y = train.Survived.values.astype(int)
X = train_processed.values
N_FEATURES = X.shape[1]


# In[11]:


classifiers = [#{'clf': LogisticRegression(), 'params': {'penalty':('l1', 'l2'), 'C': pd.np.linspace(1.e-6, 3, 20)}}, 
               {'clf': RandomForestClassifier(), 'params':{'n_estimators':[10, 50, 100, 500], 'max_depth': [2, 3, 5, 7, 11, None]}},
               #{'clf': KNeighborsClassifier(), 'params': {'n_neighbors': [1, 3, 5, 7], 'p': [1, 2]}},
               #{'clf': GaussianNB(), 'params': {'priors': [[0.7, 0.3], [0.8, 0.2]]}},
               {'clf': AdaBoostClassifier(), 'params': {'base_estimator': (DecisionTreeClassifier(max_depth=1),
                                                                           ExtraTreeClassifier(max_depth=3),
                                                                           ExtraTreeClassifier(max_depth=1),
                                                                           ExtraTreeClassifier(max_depth=5),),
                                                       'n_estimators': [20, 50, 100, 200, 500],
                                                       'algorithm': ['SAMME', 'SAMME.R'],
                                                       'learning_rate': (2.0, 1.0, 0.5, 0.05)}},
               {'clf': GradientBoostingClassifier(), 'params': {'loss': ('deviance', 'exponential'),
                                                                'n_estimators': [20, 50, 100, 200, 400],
                                                                'subsample': [1.0, 0.9],
                                                                'max_depth': [1,2,3]}},
               #{'clf': LinearDiscriminantAnalysis(), 'params': {'priors': [[0.68, 0.32]], 'n_components': [2, 4, 6]}},
               #{'clf': QuadraticDiscriminantAnalysis(), 'params': {'priors': [[0.68, 0.32]]}},
               #{'clf': SVC(gamma='scale'), 'params': {'kernel':('rbf', 'linear'), 'C': [1.0, 10.0, 100.0, 1000.0]}},
              ]
print("The number of features is ", N_FEATURES)
results = dict()
for j in range(2, 2**N_FEATURES):
    aux = SelectFeatures(j, N_FEATURES).transform(train_processed)
    print("Selected features are: ", aux.columns)
    X = aux.values
    for c in classifiers:
        print("Performing grid searching for ", c['clf'].__class__.__name__, j)
        clf = GridSearchCV(c['clf'], c['params'], cv=3, scoring='balanced_accuracy', verbose=False, n_jobs=-1);
        clf.fit(X, y)
        results[c['clf'].__class__.__name__ + '_' + str(j)] = clf
        print("Best score is ", clf.best_score_)


# In[12]:


# Select the best classifier and use it
best_classifiers = list(sorted([(k, v.best_estimator_, v.best_params_, v) for k, v in results.items()],
                          key=lambda x: x[-1].best_score_, reverse=True))[:15]
best_classifiers = [(est.__class__.__name__ + str(ind), est) for ind, est in enumerate(map(lambda x: make_pipeline(SelectFeatures(int(x[0].split('_')[-1]), N_FEATURES), x[1].__class__(**x[2])), best_classifiers))]
best = VotingClassifier(best_classifiers, n_jobs=1)
best.fit(train_processed, y)
print("Estimated score is ", cross_val_score(best, train_processed, y, cv=3).mean())


# In[13]:


submission = pd.DataFrame({
        "PassengerId": test["PassengerId"],
        "Survived": best.predict(test_processed).astype(int)
    })
submission.to_csv('./output/submission.csv', index=False)

