import pandas as pd
import numpy as np
from sklearn import preprocessing
import statsmodels.api as sm
from sklearn import model_selection
from sklearn.model_selection import cross_val_score
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
from sklearn.utils import resample
import pickle

def preprocss():
	"""
	This function includes:  
	
	1. Read data from directory.  

	2. Reduce event_type into 6 levels.  

	3. Convert assist_method into "Yes" and "No".  

	4. Upsample the data.
	"""
	data = pd.read_csv("/Users/yuecui/Desktop/ValueChain/Project/events.csv")


	t = {"other": [10,11,9,7], "FreeKick": [8], "Foul": [3], "Attempt": [1],"Card":[4,5,6],"Corner":[2]}
	t2 = {v: k for k,vv in t.items() for v in vv}
	data["event_type"] = data.event_type.map(t2).astype("category", categories=set(t2.values()))

	m = {"None": [0], "Pass": [1,2,3,4]}
	m2 = {v: k for k,vv in m.items() for v in vv}
	data["assist_method"] = data.assist_method.map(m2).astype("category", categories=set(m2.values()))


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
	 

	#####Model Fitting

	# Separate input features (X) and target variable (y)
	y = df_upsampled.is_goal
	X = df_upsampled[cols]

	y.to_csv("y.csv")
	X.to_csv("X.csv")
	return
















