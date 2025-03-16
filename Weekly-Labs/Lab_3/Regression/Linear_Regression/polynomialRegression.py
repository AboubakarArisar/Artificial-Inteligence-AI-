from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5, 6]).reshape(-1, 1)
y = np.array([3, 7, 15, 27, 43, 63])

polynomialFeatures = PolynomialFeatures(degree=2)
X_poly = polynomialFeatures.fit_transform(x)

model = LinearRegression()
model.fit(X_poly, y)

def predict_score(hours):
    hours_array = np.array([[hours]])
    hours_poly = polynomialFeatures.transform(hours_array)
    predicted_score = model.predict(hours_poly)
    return predicted_score[0]

study_hours = 7
predicted_score = predict_score(study_hours)

x_range = np.linspace(1, 7, 100).reshape(-1, 1)
x_range_poly = polynomialFeatures.transform(x_range)
y_range = model.predict(x_range_poly)

plt.scatter(x, y, color='blue', label='Actual data points')
plt.plot(x_range, y_range, color='red', label='Polynomial regression curve')
plt.scatter(study_hours, predicted_score, color='green', marker='x', s=100, label=f'Prediction: {predicted_score:.2f}')

plt.xlabel('Study Hours')
plt.ylabel('Exam Scores')
plt.title('Polynomial Regression: Study Hours vs Exam Scores')
plt.legend()
plt.grid()
plt.show()

print(f"Predicted score for {study_hours} hours of study: {predicted_score:.2f}")
