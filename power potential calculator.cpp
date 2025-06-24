// power_calculator.cpp
// Francis Turbine Power Potential Calculator

#include <iostream>
#include <iomanip>

using namespace std;

// Function to calculate power output (Watts)
double calculatePower(double density, double gravity, double discharge, double head, double efficiency) {
    return density * gravity * discharge * head * efficiency;
}

int main() {
    // Constants
    const double gravity = 9.81;        // m/s^2
    const double density = 1000.0;      // kg/m^3

    // User input
    double Q, H, eta;   // Discharge (m³/s), Head (m), Efficiency (%)

    cout << "=== Francis Turbine Power Potential Calculator ===" << endl;
    cout << "Enter discharge (Q) in m³/s: ";
    cin >> Q;

    cout << "Enter head (H) in meters: ";
    cin >> H;

    cout << "Enter efficiency (%) [e.g., 89.61 for 89.61%]: ";
    cin >> eta;

    // Convert efficiency to decimal
    eta /= 100.0;

    // Calculate power
    double powerWatts = calculatePower(density, gravity, Q, H, eta);
    double powerMW = powerWatts / 1e6;

    // Output result
    cout << fixed << setprecision(2);
    cout << "\nEstimated Power Output: " << powerMW << " MW" << endl;

    return 0;
}
