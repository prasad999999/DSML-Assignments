import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import matplotlib.pyplot as plt

df = pd.read_csv("DSMLlab/temperatures.csv")

# Convert the 'Year' column to a numeric type
df['YEAR'] = pd.to_numeric(df['YEAR'])

# Create a new DataFrame with separate columns for year and month
df_long = pd.melt(df, id_vars=['YEAR'], var_name='Month', value_name='Temperature')

# Convert the 'Month' column to a categorical type and set as the index
df_long['Month'] = pd.Categorical(df_long['Month'], categories=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
df_long.set_index(['YEAR', 'Month'], inplace=True)

# Split the data into training and testing sets
X = df_long[['YEAR', 'Month']]
y = df_long['Temperature']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Fit a linear regression model to the training data
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the testing data
y_pred = model.predict(X_test)

# Calculate the mean squared error, mean absolute error, and R^2 score of the predictions
mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean squared error: {mse:.2f}")
print(f"Mean absolute error: {mae:.2f}")
print(f"R^2 score: {r2:.2f}")

# Plot the predicted temperatures against the actual temperatures
plt.scatter(y_test, y_pred)
plt.xlabel("Actual Temperatures")
plt.ylabel("Predicted Temperatures")
plt.title("Predicted vs Actual Temperatures")
plt.show()