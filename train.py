import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

df=pd.read_csv("Employee_Salary.csv")
X=df[["Experience","SkillScore","Age"]]
y=df["Salary"]

model=LinearRegression().fit(X,y)
pickle.dump(model,open("model.pkl","wb"))
