import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

data=pd.read_csv('data.csv')
x=data[["YearsExperience"]]
y=data["Salary"]

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)


model=LinearRegression()
model.fit(x_train[['YearsExperience']],y_train)

x_test=pd.DataFrame(x_test,columns=["YearsExperience"])

ypred=model.predict(x_test)
r2=r2_score(y_test,ypred)
print("Model Training completed \n")
print("slope:", model.coef_[0])
print("intercept:", model.intercept_)
print("R2 Score:", r2)


plt.scatter(x,y)
plt.plot(x, model.predict(x), color='red', label='Regression Line')
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.title("Years of Experience vs Salary")
plt.grid()
plt.legend()
plt.show()


newexpreience=pd.DataFrame([[1.1]],columns=["YearsExperience"])
predictionsalary=model.predict(newexpreience)
print(f"predicted salary for {newexpreience.iloc[0,0]} years of experience:", predictionsalary[0])