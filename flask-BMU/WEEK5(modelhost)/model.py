# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt
# %matplotlib inline 
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression 
from sklearn import preprocessing


data = pd.read_csv("/home/bavalpreet/Documents/flask_modelhost/insurance.csv")


data.corr() # by default we get pearson correlation which lies bw -1 to 1
# 1 means highly positve relation and -1 means negative relation
# https://www.geeksforgeeks.org/python-pandas-dataframe-corr/ refer this

# LABEL ENCODING OUR DATA
le_sex = preprocessing.LabelEncoder()
data['sex']=le_sex.fit_transform(data['sex'])

le_smoker=preprocessing.LabelEncoder()
data['smoker']=le_smoker.fit_transform(data['smoker'])

le_region=preprocessing.LabelEncoder()
data['region']=le_region.fit_transform(data['region'])

output_var = 'charges'

scaler = MinMaxScaler() # Normalising our data
X = scaler.fit_transform(data[data.columns[~data.columns.isin([output_var])]])
Y = data[[output_var]]


X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.20) 


regr = LinearRegression() 
  
regr.fit(X_train, y_train) 
print(regr.score(X_test, y_test)) # R squared score

"""## saving the model"""


pickle.dump(regr,open('/home/bavalpreet/Documents/flask_modelhost/model.pkl', 'wb'))

filehandler_s = open("/home/bavalpreet/Documents/flask_modelhost/label-encoders/le_sex.pickle","wb")
filehandler_smoker=open("/home/bavalpreet/Documents/flask_modelhost/label-encoders/le_smoker.pickle","wb")
filehandler_region=open("/home/bavalpreet/Documents/flask_modelhost/label-encoders/le_region.pickle","wb")
pickle.dump(le_sex,filehandler_s)
pickle.dump(le_smoker,filehandler_smoker)
pickle.dump(le_region,filehandler_region)
filehandler_s.close()
filehandler_smoker.close()
filehandler_region.close()
