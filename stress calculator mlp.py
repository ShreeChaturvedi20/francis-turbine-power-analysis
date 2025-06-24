import numpy as np
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Simulate synthetic sensor data and stress response
np.random.seed(42)
samples = 1000

# Features: flow rate (m^3/s), torque (Nm), speed (RPM), pressure (Pa)
X = np.random.rand(samples, 4)
X[:, 0] *= 200     # Flow rate up to 200 m^3/s
X[:, 1] *= 5000    # Torque up to 5000 Nm
X[:, 2] *= 600     # Speed up to 600 RPM
X[:, 3] *= 1e6     # Pressure up to 1 MPa

# True relationship (simulated stress in MPa)
y = 0.02 * X[:, 0] + 0.004 * X[:, 1] + 0.01 * X[:, 2] + 0.00005 * X[:, 3] + np.random.normal(0, 2, samples)

# Split and train
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = MLPRegressor(hidden_layer_sizes=(64, 32), max_iter=1000, random_state=42)
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred)))
print("R² Score:", r2_score(y_test, y_pred))

# Plot results
plt.scatter(y_test, y_pred, alpha=0.6)
plt.xlabel("Actual Stress (MPa)")
plt.ylabel("Predicted Stress (MPa)")
plt.title("Stress Prediction with Neural Network")
plt.grid(True)
plt.show()
