# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 19:36:53 2020

@author: favas
"""
#importing the packages

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#reading the datafile

data=pd.read_csv('E:/fvvs/PY-DS-ML/PY-DS-ML-CM/notes/kc_house_data.csv')
dataset=data.copy()

dataset=dataset.drop(['id','date'],axis=1)

#y=dataset["price"]

y=dataset.iloc[:,0].values

del dataset["price"]

x=dataset.iloc[:,1:]

dataset.dtypes

dataset.columns

no_clm=len(dataset.columns)


numeric=dataset._get_numeric_data().columns

no_numeric=len(numeric)

#ploting hitogram for all

plt.hist(dataset["price"])
plt.hist(dataset["bedrooms"])
plt.hist(dataset["bathrooms"])
plt.hist(dataset["sqft_living"])
plt.hist(dataset["sqft_lot"])
plt.hist(dataset["floors"])
plt.hist(dataset["waterfront"])#catogorical
plt.hist(dataset["view"])#cat
plt.hist(dataset["condition"])#cat
plt.hist(dataset["grade"])#cat
plt.hist(dataset["sqft_above"])
plt.hist(dataset["sqft_basement"])
plt.hist(dataset["yr_built"])
plt.hist(dataset["yr_renovated"])
plt.hist(dataset["zipcode"])
plt.hist(dataset["lat"])
plt.hist(dataset["long"])
plt.hist(dataset["sqft_living15"])
plt.hist(dataset["sqft_lot15"])

#one hot encording for categorical variables 

"onehot Encoding is done only for the cAtegorical  data"

from sklearn import LabelEncoder,OneHotEncoder

#so here we have no need of OHC


#checking for null vallues in it

dataset.isnull()

dataset.isnull().sum()

dataset["sqft_living"]=dataset["sqft_living"].fillna(dataset["sqft_living"].mean())
dataset["sqft_lot"]=dataset["sqft_lot"].fillna(dataset["sqft_lot"].mean())
dataset["sqft_above"]=dataset["sqft_above"].fillna(dataset["sqft_above"].mean())
dataset["yr_built"]=dataset["yr_built"].fillna(dataset["yr_built"].mean())


#box plot for out layers

plt.boxplot(dataset["price"])
plt.boxplot(dataset["bedrooms"])
plt.boxplot(dataset["bathrooms"])
plt.boxplot(dataset["sqft_living"])
plt.boxplot(dataset["sqft_lot"])
plt.boxplot(dataset["floors"])
plt.boxplot(dataset["waterfront"])
plt.boxplot(dataset["view"])
plt.boxplot(dataset["condition"])
plt.boxplot(dataset["grade"])
plt.boxplot(dataset["sqft_above"])
plt.boxplot(dataset["sqft_basement"])
plt.boxplot(dataset["yr_built"])
plt.boxplot(dataset["yr_renovated"])#no
plt.boxplot(dataset["zipcode"])
plt.boxplot(dataset["lat"])#no
plt.boxplot(dataset["long"])
plt.boxplot(dataset["sqft_living15"])
plt.boxplot(dataset["sqft_lot15"])


#we need to remove the out layers
percentile=dataset["price"].quantile([0.1,0.9]).values
dataset["price"]=dataset["price"].clip(percentile[0],percentile[1])

percentile=dataset["bedrooms"].quantile([0.1,0.9]).values
dataset["bedrooms"]=dataset["bedrooms"].clip(percentile[0],percentile[1])

percentile=dataset["bathrooms"].quantile([0.1,0.9]).values
dataset["bathrooms"]=dataset["bathrooms"].clip(percentile[0],percentile[1])

percentile=dataset["sqft_living"].quantile([0.1,0.9]).values
dataset["sqft_living"]=dataset["sqft_living"].clip(percentile[0],percentile[1])

percentile=dataset["sqft_lot"].quantile([0.1,0.9]).values
dataset["sqft_lot"]=dataset["sqft_lot"].clip(percentile[0],percentile[1])

percentile=dataset["floors"].quantile([0.1,0.9]).values
dataset["floors"]=dataset["floors"].clip(percentile[0],percentile[1])

percentile=dataset["waterfront"].quantile([0.1,0.9]).values
dataset["waterfront"]=dataset["waterfront"].clip(percentile[0],percentile[1])

percentile=dataset["view"].quantile([0.1,0.9]).values
dataset["view"]=dataset["view"].clip(percentile[0],percentile[1])

percentile=dataset["condition"].quantile([0.1,0.9]).values
dataset["condition"]=dataset["condition"].clip(percentile[0],percentile[1])

percentile=dataset["grade"].quantile([0.1,0.9]).values
dataset["grade"]=dataset["grade"].clip(percentile[0],percentile[1])

percentile=dataset["sqft_above"].quantile([0.1,0.9]).values
dataset["sqft_above"]=dataset["sqft_above"].clip(percentile[0],percentile[1])

percentile=dataset["sqft_basement"].quantile([0.1,0.9]).values
dataset["sqft_basement"]=dataset["sqft_basement"].clip(percentile[0],percentile[1])

percentile=dataset["yr_built"].quantile([0.1,0.9]).values
dataset["yr_built"]=dataset["yr_built"].clip(percentile[0],percentile[1])

percentile=dataset["zipcode"].quantile([0.1,0.9]).values
dataset["zipcode"]=dataset["zipcode"].clip(percentile[0],percentile[1])

percentile=dataset["long"].quantile([0.1,0.9]).values
dataset["long"]=dataset["long"].clip(percentile[0],percentile[1])

percentile=dataset["sqft_living15"].quantile([0.1,0.9]).values
dataset["sqft_living15"]=dataset["sqft_living15"].clip(percentile[0],percentile[1])

percentile=dataset["sqft_lot15"].quantile([0.1,0.9]).values
dataset["sqft_lot15"]=dataset["sqft_lot15"].clip(percentile[0],percentile[1])


#OHEC for all catogorical variable and removing its dummy variables tooo

wf=pd.get_dummies(dataset["waterfront"],prefix="wf",drop_first=True)

vw=pd.get_dummies(dataset["view"],prefix="vw",drop_first=True)

cdn=pd.get_dummies(dataset["condition"],prefix="cdn",drop_first=True)

zpc=pd.get_dummies(dataset["zipcode"],prefix="zpc",drop_first=True)


dataset=pd.concat([wf,vw,cdn,zpc],axis=1)

del dataset["waterfront"]
del dataset["view"]
del dataset["condition"]
del dataset["zipcode"]

y=dataset.iloc[:,0].values

x=dataset.iloc[:,1:]


from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)

import statsmodels.api as sm

x_train_sm=sm.add_constant(x_train)
x_test_sm=sm.add_constant(x_test)

from sklearn.metrics import r2_score

model=sm.OLS(y_train,x_train_sm).fit()
prediction=model.predict(x_test_sm)

r2=r2_score(y_test,prediction)

model.summary()















