# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 12:26:01 2019

@author: favas
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 11:45:13 2019

@author: favas
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv('D:\PY-DS-ML-CM\Auto-mpg.csv',na_values=['?','n.a'])

data_copy=data.copy()

#finding number of numerical colomns in the data

nume_data=data_copy._get_numeric_data().columns

nume_data[1]

len_numdata=len(nume_data)
#ploting histogram for all numerical to check type(categorical/continues)

#'mpg', 'cylinders', 'displacement', 'weight', 'acceleration','model year', 'origin'
'''
plt.hist(data["displacement"])

plt.hist(data["cylinders"])


plt.hist(data["weight"])


plt.hist(data["acceleration"])

plt.hist(data["mpg"])

plt.hist(data["model year"])

plt.hist(data["origin"])

plt.hist(data["horsepower"])
'''
for i in range(0,len_numdata):
    plt.hist(data[nume_data[i]])
    
#ploting density normal for the continues data
'''
sns.kdeplot(data["displacement"])

sns.kdeplot(data["weight"])

sns.kdeplot(data["acceleration"])

sns.kdeplot(data["model year"])
'''

for i in range(0,len_numdata):
    sns.kdeplot(data[nume_data[i]])

#data1=data.replace('?','NaN')
data.isnull().sum()

#replace nan with mean according to it

data["horsepower"]=data["horsepower"].fillna(data["horsepower"].mean())

#after removing the out NaN checking the boxplot

plt.boxplot(data['displacement'])

plt.boxplot(data['cylinders'])

plt.boxplot(data['weight'])

plt.boxplot(data['acceleration'])

plt.boxplot(data['model year'])

plt.boxplot(data['origin'])

plt.boxplot(data['horsepower'])

plt.boxplot(data['mpg'])


#replacing out layers with Quartile values

percentile=data['acceleration'].quantile([0.1,0.9]).values

data['acceleration']=data['acceleration'].clip(percentile[0],percentile[1])

percentile=data['horsepower'].quantile([0.1,0.9]).values

data['horsepower']=data['horsepower'].clip(percentile[0],percentile[1])

percentile=data['mpg'].quantile([0.1,0.9]).values

data['mpg']=data['mpg'].clip(percentile[0],percentile[1])

#after replacing the outlayers ,we can see some goo boxplotsfor above

#then we go and analysis the carname colm and we decide that colmn make no sence
data.columns#list ou all columns
del data["car name"]

#now we have 2 categorical data int the set so we go fot OHC

dummy_cyl=pd.get_dummies(data["cylinders"],prefix="cyl")

dummy_orgn=pd.get_dummies(data["origin"],prefix="orgn")

#addting those dummy data into our original data and removimg the curresponding parrent colmn of dummies

data_ohc=pd.concat([data,dummy_cyl,dummy_orgn],axis=1)

del data_ohc["cylinders"]

del data_ohc["origin"]

"""above what we did with the data is called as DATA PREPROCESSING"""

"""now we can do the analysis with the final data ie:data_ohc"""

y_ohc=data_ohc["mpg"]
del data_ohc["mpg"]
x_ohc=data_ohc.copy()
 #spliting x and y data into test and train
 
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x_ohc,y_ohc,test_size=0.2,random_state=0)

#now here we can go for linear regression but i am go for statmodel

import statsmodels.api as sm

x_train_sm=sm.add_constant(x_train)
x_test_sm=sm.add_constant(x_test)

"""now the problem for statsmodels hove no constnt is solved and we are ready to go"""
#creating model and predicting the test

#if we want r2 value so we need to import it

from sklearn.metrics import r2_score

model=sm.OLS(y_train,x_train_sm).fit()

prediction=model.predict(x_test_sm)

r2=r2_score(y_test,prediction)

model.summary()








