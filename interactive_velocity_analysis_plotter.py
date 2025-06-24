import numpy as np
import matplotlib.pyplot as plt

def draw_velocity_triangle(V, U, beta_deg, position='Inlet'):
    beta_rad = np.deg2rad(beta_deg)

    # Vector breakdown
    Vx = V * np.cos(beta_rad)   # Axial (flow)
    Vy = V * np.sin(beta_rad)   # Tangential
    Wx = Vx                     # Relative axial velocity
    Wy = Vy - U                 # Relative tangential = absolute - blade

    # Origin
    origin = np.array([0, 0])

    # V vector
    V_vec = np.array([Vx, Vy])
    # U vector (along tangential only)
    U_vec = np.array([0, U])
    # W vector (relative velocity)
    W_vec = np.array([Wx, Wy])

    # Plot setup
    plt.figure(figsize=(6, 6))
    plt.quiver(*origin, *V_vec, angles='xy', scale_units='xy', scale=1, color='blue', label='Absolute Velocity (V)')
    plt.quiver(*origin, *U_vec, angles='xy', scale_units='xy', scale=1, color='green', label='Blade Velocity (U)')
    plt.quiver(*origin, *W_vec, angles='xy', scale_units='xy', scale=1, color='red', label='Relative Velocity (W)')

    plt.title(f"{position} Velocity Triangle")
    plt.grid()
    plt.axis('equal')
    plt.xlim(-U - 5, V + 10)
    plt.ylim(-V, V + 10)
    plt.legend()
    plt.xlabel("Axial Direction")
    plt.ylabel("Tangential Direction")
    plt.show()

# Example: Inlet triangle (V=25 m/s, U=15 m/s, beta=65°)
draw_velocity_triangle(V=25, U=15, beta_deg=65, position='Inlet')

# You can repeat for Outlet: draw_velocity_triangle(V=20, U=12, beta_deg=110, position='Outlet')
