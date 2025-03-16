import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, PolynomialFeatures, StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.neighbors import KNeighborsRegressor

df = pd.read_csv("sales.csv")

print("Dataset Columns:", df.columns)

print("Enter the column names for the independent variables (comma-separated):")
x_cols = input().strip().split(',')
print("Enter the column name for the dependent variable:")
y_col = input().strip()

for col in x_cols:
    if df[col].dtype == 'object':
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])

X = df[x_cols]
y = df[y_col]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

def fit_polynomial(degree):
    model = make_pipeline(PolynomialFeatures(degree), LinearRegression())
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    return mse, r2, y_pred

mse_deg2, r2_deg2, y_pred_deg2 = fit_polynomial(2)
mse_deg3, r2_deg3, y_pred_deg3 = fit_polynomial(3)

print(f"Degree 2 - Mean Squared Error: {mse_deg2}, R-squared Score: {r2_deg2}")
print(f"Degree 3 - Mean Squared Error: {mse_deg3}, R-squared Score: {r2_deg3}")

knn_model = make_pipeline(StandardScaler(), KNeighborsRegressor(n_neighbors=5))
knn_model.fit(X_train, y_train)
y_pred_knn = knn_model.predict(X_test)
mse_knn = mean_squared_error(y_test, y_pred_knn)
r2_knn = r2_score(y_test, y_pred_knn)

print(f"KNN - Mean Squared Error: {mse_knn}, R-squared Score: {r2_knn}")

plt.scatter(y_test, y_pred_deg2, color='blue', label='Degree 2 Predictions', alpha=0.5)
plt.scatter(y_test, y_pred_deg3, color='red', label='Degree 3 Predictions', alpha=0.5)
plt.scatter(y_test, y_pred_knn, color='green', label='KNN Predictions', alpha=0.5)
plt.xlabel('Actual Values')
plt.ylabel('Predicted Values')
plt.title('Regression Model Comparison')
plt.legend()
plt.show()