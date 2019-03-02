from sklearn import tree

#Is a Descition tree

#[Height, Weight, Size shoe]
x = [[181,80,44], [177,70,43],[160,60,38],[190,23,15],[180,56,36],[190,56,78]]
y = ['male','female','female','male','female','male']
#Setup the decision tree
clf = tree.DecisionTreeClassifier()
#train our model
clf = clf.fit(x,y)

prediction = clf.predict([[160,56,34]])
print(prediction)

