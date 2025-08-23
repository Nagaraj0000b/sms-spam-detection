import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import confusion_matrix, mean_squared_error, r2_score

diabeties_data=pd.read_csv('diabetes.csv')

x=diabeties_data[['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age']]
y=diabeties_data['Outcome']


x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)



model=LinearRegression()
model.fit(x_train,y_train)


y_pred=model.predict(x_test)


y_pred_binary = (y_pred >= 0.5).astype(int)

accuracy=accuracy_score(y_test, y_pred_binary)
conf_matrix = confusion_matrix(y_test, y_pred_binary)

print("Accuracy:", accuracy)
print("Confusion Matrix:\n", conf_matrix)

new_patient = pd.DataFrame({
    # Provided row: 5,116,74,0,0,25.6,0.201,30,0 (Outcome not used for prediction)
    'Pregnancies': [5],
    'Glucose': [116],
    'BloodPressure': [74],
    'SkinThickness': [0],
    'Insulin': [0],
    'BMI': [25.6],
    'DiabetesPedigreeFunction': [0.201],
    'Age': [30]
})
prediction = model.predict(new_patient)
pred_val = float(prediction[0])  # extract scalar from 1D array
prediction_binary = int(pred_val >= 0.5)
print(f"Raw prediction value: {pred_val:.4f}")
print("Prediction for new patient (1: Diabetic, 0: Non-Diabetic):", prediction_binary)