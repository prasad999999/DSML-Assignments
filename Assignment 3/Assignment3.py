from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error

df = pd.read_csv('Customers.csv')

x = df[['Gender', 'Age', 'Annual Income ($)', 'Work Experience']]
y = df['Spending Score (1-100)']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

model = KNeighborsRegressor(n_neighbors=3)
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

mse = mean_squared_error(y_test, y_pred)

print("Mean Squared Error:", mse)