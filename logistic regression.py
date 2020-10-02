import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#reading dataset

org_dataset=pd.read_csv('D:\PY-DS-ML-CM\P12-50-Startups.CSV')

dataset=org_dataset.copy()

#extracting target and dataset

Y=dataset['Profit'].values

del dataset['Profit']

X=dataset.values

#encording categorical variables

from sklearn.preprocessing import LabelEncoder, OneHotEncoder

labelencoder = LabelEncoder()

X[:, 3] = labelencoder.fit_transform(X[:, 3])

onehotencoder = OneHotEncoder(categorical_features = [3])

X = onehotencoder.fit_transform(X).toarray()

# Avoiding the Dummy Variable Trap
X = X[:, 1:]

# Splitting the dataset into the Training set and Test set

from sklearn.model_selection import train_test_split

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=0)


from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, Y_train)

regressor.intercept_
regressor.coef_

#predictng x-test with this model

predct=regressor.predict(X_test)
 



#vere oru metod nd

import statsmodels.api as sm
from sklearn.metrics import r2_score

#stst modelil mx+c yile c ne edkoola so we need to add it as aconstant for our dataset


X_train=sm.add_constant(X_train)
X_test=sm.add_constant(X_test)

model=sm.OLS(Y_train,X_train).fit()

predictor=model.predict(X_test)

r2_ohc=r2_score(Y_test,predictor)

model.summary()





