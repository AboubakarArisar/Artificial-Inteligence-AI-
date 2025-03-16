import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("sales.csv")


print("Dataset Columns:", df.columns)

print("Enter the column name for the independent variable : ")
x_col = input().strip()
print("Enter the column name for the dependent variable : ")
y_col = input().strip()
if df[x_col].dtype == 'object':
    le = LabelEncoder()
    df[x_col] = le.fit_transform(df[x_col])
X = df[[x_col]]
y = df[y_col]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R-squared Score: {r2}")

plt.scatter(X_test, y_test, color='blue', label='Actual Values')
plt.plot(X_test, y_pred, color='red', linewidth=2, label='Regression Line')
plt.xlabel(x_col)
plt.ylabel(y_col)
plt.title('Simple Linear Regression')
plt.legend()
plt.show()
