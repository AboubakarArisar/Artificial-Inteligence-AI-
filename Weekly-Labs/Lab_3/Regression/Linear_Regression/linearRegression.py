from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Create a linear regression model (sample data : study hours v exam scores)

x = [[1], [2], [3], [4], [5]]
y = [10, 20, 30, 40, 50]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

# print(x_train)
# print(x_test)
# print(y_train)
# print(y_test)

model = LinearRegression()
model.fit(x_train, y_train)

predicted = model.predict(x_test)

print("Predicted values: ", predicted)
