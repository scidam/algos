'''


'''

__author__ = 'Dmitry E. Kislov'
__email__ = 'kislov@easydan.com'


import time
import tensorflow as tf

# Load mnist data and show some data properties
mnist = tf.keras.datasets.mnist

(x_train, y_train),(x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

print("Shape of x_train is ", x_train.shape)
print("Shape of x_test is ", x_test.shape)


# Importing the most using classifiers from scikit-learn
from sklearn.ensemble import (RandomForestClassifier, AdaBoostClassifier,
                              ExtraTreesClassifier)
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB, MultinomialNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.decomposition import PCA, KernelPCA


from sklearn.pipeline import make_pipeline
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score

import xgboost as xgb


STANDARD_CLASSIFIERS = (
                        {'method': xgb.XGBClassifier,
                         'parameters': {'max_depth': 5, 'n_jobs': 2}
                         },
                        
                        {'method' : RandomForestClassifier,
                         'parameters' : {'n_estimators': 10, 'max_depth': 4, 'random_state': 0}
                        },
                        
                        {'method' : RandomForestClassifier,
                         'parameters' : {'n_estimators': 50, 'max_depth': 4, 'random_state': 0}
                        },
                        
                        {'method' : RandomForestClassifier,
                         'parameters' : {'n_estimators': 50, 'max_depth': 20, 'random_state': 0}
                        },
                        
                        {'method' : RandomForestClassifier,
                         'parameters' : {'n_estimators': 100, 'max_depth': 4, 'random_state': 0}
                        },
                        
                        {'method' : RandomForestClassifier,
                         'parameters' : {'n_estimators': 100, 'max_depth': 20, 'random_state': 0}
                        },
                        
                        {'method': ExtraTreesClassifier,
                          'parameters': {'n_estimators': 10, 'max_depth': None, 'random_state': 0}
                        },

                        {'method': ExtraTreesClassifier,
                          'parameters': {'n_estimators': 100, 'max_depth': 10, 'random_state': 0}
                        },
                        
                        {'method': LogisticRegression,
                         'parameters': {'C': 1.0,  'penalty': 'l2', 'random_state': 0}
                        },
                        
                        {'method': LogisticRegression,
                         'parameters': {'C': 0.5,  'penalty': 'l2', 'random_state': 0}
                        },

                        {'method': LogisticRegression,
                         'parameters': {'C': 0.01, 'penalty': 'l2',  'random_state': 0}
                        },
                        
                        {'method': LogisticRegression,
                         'parameters': {'C': 0.001, 'penalty': 'l2', 'random_state': 0}
                        },
                        
                        {'method': LogisticRegression,
                         'parameters': {'C': 1.0, 'penalty': 'l1',  'random_state': 0}
                        },
                        
                        {'method': LogisticRegression,
                         'parameters': {'C': 0.5,  'penalty': 'l1', 'random_state': 0}
                        },

                        {'method': LogisticRegression,
                         'parameters': {'C': 0.01, 'penalty': 'l1', 'random_state': 0}
                        },
                        
                        {'method': LogisticRegression,
                         'parameters': {'C': 0.001, 'penalty': 'l1', 'random_state': 0}
                        },

                        {'method': GaussianNB,
                         'parameters': dict(),
                        },
                        
                        {'method': MultinomialNB,
                         'parameters': dict(),
                        },
                        
                        {'method': KNeighborsClassifier,
                         'parameters': {'n_neighbors': 1, 'n_jobs': -1},
                        },
                        
                        {'method': KNeighborsClassifier,
                         'parameters': {'n_neighbors': 5, 'n_jobs': -1},
                        },
                        
                        {'method': KNeighborsClassifier,
                         'parameters': {'n_neighbors': 20, 'n_jobs': -1},
                        },
                        
                        {'method': SVC,
                         'parameters': {'kernel': 'linear', 'C': 0.025, 'random_state': 0},
                        },
                        
                        {'method': SVC,
                         'parameters': {'gamma': '2', 'C': 1.0, 'random_state': 0},
                        },
                        
                        {'method': QuadraticDiscriminantAnalysis,
                         'parameters': dict(),
                        },
                        
                        {'method': MLPClassifier,
                         'parameters': dict(),
                        },
                        
                        
                       )

PREPROCESSING_METHODS = (
    
                        {'method': '',
                         'parameters': dict()
                        },
                        
                        {'method': PCA,
                         'parameters': {'n_components': 10 }
                        },
                        
                        {'method': PCA,
                         'parameters': {'n_components': 5 }
                        },
                        
                        {'method': KernelPCA,
                         'parameters': {'n_components': 10, 'kernel': 'linear'}
                        },
               
                        {'method': KernelPCA,
                         'parameters': {'n_components': 10, 'kernel': 'rbf'}
                        },

                        )


num_pixels = x_train.shape[-1] * x_train.shape[-2]
x_train_reshaped = x_train.reshape(x_train.shape[0], num_pixels)
x_test_reshaped = x_test.reshape(x_test.shape[0], num_pixels)


def make_info_string(clf, clf_pars, prep, prep_pars):
    if preprocessor['method']:
        preprocessor_name = preprocessor['method'].__name__
    else:
        preprocessor_name = ''
    
    if preprocessor_name:
        res = 'Evaluating {} with preprocessing step {}.'.format(clf.__name__ + '(' + clf_pars.__str__() + ')',
                                                                 prep.__name__ + '(' + prep_pars.__str__() + ')')
    else:
        res = 'Evaluating {}.'.format(clf.__name__ + '(' + clf_pars.__str__() + ')')
    
    return res, preprocessor_name


for classificator in STANDARD_CLASSIFIERS:
    for preprocessor in PREPROCESSING_METHODS:
        start = time.time()
        if preprocessor['method']:
            clf = make_pipeline(preprocessor['method'](**preprocessor['parameters']), classificator['method'](**classificator['parameters']))
        else:
            clf = classificator['method'](**classificator['parameters'])
        s, preprocessor_name = make_info_string(classificator['method'], classificator['parameters'], preprocessor['method'], preprocessor['parameters'])
        try:
            clf.fit(x_train_reshaped, y_train)
            y_pred = clf.predict(x_test_reshaped)
            accuracy = accuracy_score(y_test, y_pred)
        except:
            print("Something got wrong with the pair (classifier, preprocessor): ({}, {})".format(classificator['method'].__name__, preprocessor_name)), 
            print("Parameters were ({}, {}):".format(classificator['parameters'], preprocessor['parameters']))
            accuracy = None
        if accuracy:
            print(s)
            print("Accuracy: ", accuracy)
        end = time.time()
        print("Elapsed time: ", end - start)
        print("-" * 100)
