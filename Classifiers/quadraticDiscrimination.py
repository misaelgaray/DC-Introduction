from sklearn import discriminant_analysis

x = [[181, 80, 44],[160, 76, 39],[172, 79, 43],[190, 90, 48],[150, 50, 35],[170, 65, 35],[168, 56, 29],[159, 49, 27]]
y = ['male','male','male','male','female','female','female','female']

clf = discriminant_analysis.QuadraticDiscriminantAnalysis()
clf = clf.fit(x,y)

#Should be a big male
print(clf.predict([[210,100,50]]))

#Could be a thin man or a big female
print(clf.predict([[171,68,37]]))

#Should be a thin female
print(clf.predict([[150,40,20]]))
