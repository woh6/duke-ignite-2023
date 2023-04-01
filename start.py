import numpy as np #some helpful math functions
import pandas as pd #helps import data as 2D array
import matplotlib.pyplot as plt #plotting tools
import seaborn as sb #other visualization tools

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from xgboost import XGBClassifier #has eXtreme Gradient Boosting machine learning algorithm which improves precision
from sklearn import metrics

import warnings
warnings.filterwarnings('ignore')
