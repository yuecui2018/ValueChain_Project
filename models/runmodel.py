def runmodel():
	"""
	This function includes:  
	
	1. Split data into training and testing. 

	2. Train the model using logistic regression. 

	3. Output the summary result. 

	4. Save the model result into pickle file. 
	"""
	
	X = pd.read_csv("X.csv")
	y = pd.read_csv("y.csv")
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

	kfold = model_selection.KFold(n_splits=10, random_state=7)
	modelCV = LogisticRegression()
	scoring = 'accuracy'

	results = model_selection.cross_val_score(modelCV, X_train, y_train, cv=kfold, scoring=scoring)
	print("10-fold cross validation average accuracy: %.3f" % (results.mean()))

	logit_model=sm.Logit(y,X)
	result=logit_model.fit()
	print(result.summary())
	pickle.dump(result, open("/Users/yuecui/Documents/GitHub/ValueChain_Project/soccer_event/src/models/result.p","wb"))

	return