#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 14:43:08 2018

@author: yuecui
"""

import pandas as pd
import numpy as np
from sklearn import preprocessing
import matplotlib.pyplot as plt 
plt.rc("font", size=14)

from sklearn.cross_validation import train_test_split
import seaborn as sns
sns.set(style="white")
sns.set(style="whitegrid", color_codes=True)
import matplotlib.pyplot as plt

from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression

from scipy import stats
import statsmodels.api as sm


from sklearn import model_selection
from sklearn.model_selection import cross_val_score

from sklearn.utils import resample
###Read data
data = pd.read_csv("/Users/yuecui/Desktop/ValueChain/Project/events.csv")

data = data[["time","side","event_type","assist_method","fast_break","is_goal"]]

"""
8     0.252848
3     0.247527
1     0.243499
2     0.096921
7     0.054981
9     0.046201
4     0.042413
10    0.011403
11    0.002876
6     0.001224
5     0.000106
"""

m = {"other": [10,11,9,7], "FreeKick": [8], "Foul": [3], "Attempt": [1],"Card":[4,5,6],"Corner":[2]}

m2 = {v: k for k,vv in m.items() for v in vv}
m2

data["event_type"] = data.event_type.map(m2).astype("category", categories=set(m2.values()))

data["event_type"].value_counts()/941009


sns.countplot(x="event_type", data=data)
plt.show()


"""
5    237932   
2    232925
1    229135
3    108650
0     91204
4     41163
"""
"""
FreeKick    0.252848
Foul        0.247527
Attempt     0.243499
other       0.115461
Corner      0.096921
Card        0.043743
"""



"""
assist_method
0	None
1	Pass
2	Cross
3	Headed pass
4	Through ball
"""

data['assist_method'].value_counts()/data['assist_method'].value_counts().sum()

m = {"None": [0], "Pass": [1,2,3,4]}

m2 = {v: k for k,vv in m.items() for v in vv}
m2

data["assist_method"] = data.assist_method.map(m2).astype("category", categories=set(m2.values()))

data["assist_method"].value_counts()/941009

sns.countplot(x="assist_method", data=data)
plt.show()

"""
1    773104 None
0    167905 Pass
"""




"""
fast_break
"""
data['fast_break'].value_counts()
plt.hist(data['fast_break'])



#####categorical to dummies


cat_vars=["event_type","fast_break","side","assist_method"]
for var in cat_vars:
    cat_list='var'+'_'+var
    cat_list = pd.get_dummies(data[var], prefix=var)
    data1=data.join(cat_list)
    data=data1
cat_vars=["event_type","fast_break","side","assist_method"]

data_vars=data.columns.values.tolist()

to_keep = list(set(data_vars).difference(set(cat_vars)))


data_final=data[to_keep]
data_final.columns.values


data_final_vars=data_final.columns.values.tolist()
y=['is_goal']
X=[i for i in data_final_vars if i not in y]
len(X)
#####Feature Selection 



logreg = LogisticRegression()
rfe = RFE(logreg, 13)
rfe = rfe.fit(data_final[X], data_final[y] )
print(rfe.support_)
print(rfe.ranking_)


#####Model Building

stats.chisqprob = lambda chisq, df: stats.chi2.sf(chisq, df)
logit_model=sm.Logit(data_final.is_goal,data_final[X])
result=logit_model.fit()
print(result.summary())

cols=['event_type_FreeKick',
      'event_type_Corner',
 'event_type_Attempt',
 'time',
 'assist_method_Pass',
 'event_type_Foul',
 'event_type_Card',
 'side_2',
 'event_type_other',
 'fast_break_1']

X=data[cols]
y=data['is_goal']

logit_model=sm.Logit(y,X)
result=logit_model.fit()
print(result.summary())

# Separate majority and minority classes
df_majority = data[data.is_goal==0]
df_minority = data[data.is_goal==1]

# Upsample minority class
df_minority_upsampled = resample(df_minority, 
                                 replace=True,     # sample with replacement
                                 n_samples=916563,    # to match majority class
                                 random_state=123) # reproducible results

# Combine majority class with upsampled minority class
df_upsampled = pd.concat([df_majority, df_minority_upsampled])
 
# Display new class counts
df_upsampled.is_goal.value_counts()


#####Model Fitting

# Separate input features (X) and target variable (y)
y = df_upsampled.is_goal
X = df_upsampled[cols]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

logreg = LogisticRegression()
logreg.fit(X_train, y_train)


y_pred = logreg.predict(X_test)
print('Accuracy of logistic regression classifier on test set: {:.2f}'.format(logreg.score(X_test, y_test)))



kfold = model_selection.KFold(n_splits=10, random_state=7)
modelCV = LogisticRegression()
scoring = 'accuracy'

results = model_selection.cross_val_score(modelCV, X_train, y_train, cv=kfold, scoring=scoring)
print("10-fold cross validation average accuracy: %.3f" % (results.mean()))


print(result.summary())






result = logreg.fit


print(result.summary())

pred_prob=float(result.predict([1,1,0,34,0,0,0,0,0,0]))

import pickle
pickle.dump(result, open("/Users/yuecui/Documents/GitHub/ValueChain_Project/soccer_event/src/models/result.p","wb"))






