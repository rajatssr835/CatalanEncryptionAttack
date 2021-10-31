import matplotlib
import sklearn
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import matthews_corrcoef
import pandas as pd
import numpy as np
from sklearn import svm
import matplotlib.pyplot as plt
from sklearn.model_selection import validation_curve
from sklearn.svm import SVR
from sklearn.metrics import confusion_matrix
from sklearn.linear_model import LassoCV
from sklearn import metrics
from sklearn.metrics import accuracy_score
import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from google.colab import files
from yellowbrick.model_selection import LearningCurve
from sklearn import tree
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestRegressor

#files.upload()
data = pd.read_csv('dataset.csv', header=None, usecols=[i for i in range(32)])
# the usecols=[i for i in range(11)] will create a list of numbers for your columns
# that line will make a dataframe called data, which will contain your data.
l = [i for i in range(16)]
X = data[l]
for a in range(16):
 y = data[16+a]
 lw=2
 X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20)
 
 regressor = SVR(kernel='poly', C=1e3, degree=3)
 regressor.fit(X_train,y_train)


 y_pred = regressor.predict(X_test)

 print(cross_val_score(regressor, X, y, cv=10))
 y = pd.Series(y_test)
 x = pd.Series(y_pred)
 # plotting the data
 
 print(y.corr(x))
   
 #print("MSE:", mean_squared_error(y_test, y_pred))
 print("R2 score : %.2f" % r2_score(y_test,y_pred))
 #print('Accuracy: %.3f' % accuracy_score(y_test, y_pred))
 plt.scatter(range(len(X_test)), y_test, color="darkorange", label="Actual Bit")
 plt.scatter(range(len(X_test)), y_pred, color="navy", label="Model Predicted Bit")
 plt.xlabel("Plaintext")
 plt.ylabel("Ciphertext Bit")
 #plt.title("Support Vector Regression")
 plt.legend()
 plt.show()
 regressor1=svm.SVC(C=1, kernel='linear')
 regressor1.fit(X_train,y_train)
 y_pred = regressor1.predict(X_test)
 print(confusion_matrix(y_test,y_pred))
 y_pred = regressor1.predict(X_test)
 regr1 = RandomForestRegressor(max_depth=2, random_state=0)
 regr1.fit(X_train,y_train)
 print("mathew")
 print(matthews_corrcoef(y_test, y_pred))
 print(confusion_matrix(y_test,y_pred))
 y_pred = regr1.predict(X_test)

 print("R2 score : %.2f" % r2_score(y_test,y_pred))
 regr1 = LassoCV( random_state=0).fit(X_train,y_train)
 y_pred = regr1.predict(X_test)
 print("R2 score : %.2f" % r2_score(y_test,y_pred))


