import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report, confusion_matrix

# Generate synthetic vibration signals
def simulate_signal(cavitating, length=1024):
    freq = np.fft.fftfreq(length)
    if cavitating:
        signal = np.random.normal(0, 1.5, length) + np.sin(2*np.pi*50*np.linspace(0, 1, length))
    else:
        signal = np.random.normal(0, 0.5, length) + np.sin(2*np.pi*10*np.linspace(0, 1, length))
    return np.abs(np.fft.fft(signal))[:length // 2]

# Create dataset
X = np.array([simulate_signal(i % 2) for i in range(1000)])
y = np.array([i % 2 for i in range(1000)])

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train MLP
model = MLPClassifier(hidden_layer_sizes=(64, 32), max_iter=300, random_state=42)
model.fit(X_train, y_train)

# Evaluation
y_pred = model.predict(X_test)
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Plot example signals
plt.figure(figsize=(10, 4))
plt.plot(simulate_signal(0), label="Non-Cavitating")
plt.plot(simulate_signal(1), label="Cavitating")
plt.legend()
plt.title("Synthetic Vibration Signals")
plt.show()
