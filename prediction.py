#CODE
from sklearn import tree
from random import randint
import random
i=0
X=[]
Y=[]
gender = ['male','female']
while i < 8 :
    i = i + 1
    x = [randint(160,180),randint(60,80),randint(36,45)]
    X.append(x)
    y = [ random.choice(gender)]
    Y.append(y)
print(X)
print(Y)

clf= tree.DecisionTreeClassifier()
clf=clf.fit(X,Y)
predict= clf.predict([[190,70,43]])
print(predict)
