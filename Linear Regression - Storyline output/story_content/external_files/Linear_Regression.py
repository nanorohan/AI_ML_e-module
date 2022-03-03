# -*- coding: utf-8 -*-
"""Linear_Regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17LWSoaNUjlvIxGGNYcxuraxsbn1xpiis
"""

import pandas as pd

Machining = pd.read_csv('Machining.csv')

Machining

Machining.shape

X = Machining.drop(columns = ['Finish'])
y = Machining['Finish']

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

from sklearn.impute import SimpleImputer
import numpy as np

imputer = SimpleImputer(missing_values=np.nan, strategy='median')
imputer.fit(X_train)
X_train = imputer.transform(X_train)

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)

from sklearn.linear_model import LinearRegression

regressor = LinearRegression()
regressor.fit(X_train, y_train)

X_test = imputer.transform(X_test)
X_test = scaler.transform(X_test)
y_pred = regressor.predict(X_test)

y_pred[0:40]

y_test.values[0:40]