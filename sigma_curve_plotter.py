import matplotlib.pyplot as plt
import numpy as np

# Simulated data (you can replace these with SimScale outputs)
sigma_vals = np.linspace(0.05, 0.25, 50)

# Example efficiency curves
eff_part = 0.91 - 0.4 * (sigma_vals - 0.18)**2
eff_rated = 0.94 - 0.25 * (sigma_vals - 0.12)**2
eff_over = 0.89 - 0.3 * (sigma_vals - 0.16)**2

# Clip efficiencies to [0, 1]
eff_part = np.clip(eff_part, 0, 1)
eff_rated = np.clip(eff_rated, 0, 1)
eff_over = np.clip(eff_over, 0, 1)

# Plotting
plt.figure(figsize=(10,6))
plt.plot(sigma_vals, eff_part, label='Part Load', linestyle='--', color='blue')
plt.plot(sigma_vals, eff_rated, label='Rated Load', linestyle='-', color='green')
plt.plot(sigma_vals, eff_over, label='Over Load', linestyle='-.', color='red')

plt.xlabel('Cavitation Number (σ)')
plt.ylabel('Hydraulic Efficiency')
plt.title('Sigma Curve Analysis – Cavitation Performance')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
