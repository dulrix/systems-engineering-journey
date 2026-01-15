


# This program simulates a basic electrical energy system over a 24-hour period.
# A constant voltage is assumed, while the current varies throughout the day between approximately 3–7 amps to model real-world load fluctuations.
# Power is calculated using the standard electrical relationship between voltage and current, and total energy consumption is computed by integrating power over time.
# Finally, the system behavior is visualized using plots of current vs time and power vs time.




# Import numpy for numerical operations
import numpy as np
# Import matplotlib for plotting graphs
import matplotlib.pyplot as plt

# Create an array of time in hours from 0 to 24 (inclusive) with 25 points
time_hours = np.linspace(0, 24, 25)

# Assign a constant voltage of 230V for each time point
voltage = np.full_like(time_hours, 230)

# Calculate current as a sinusoidal function with base 5A and amplitude 2A
current = 5 + 2 * np.sin(2 * np.pi * time_hours / 24)

# Compute instantaneous power using P = V * I
power = voltage * current

# Calculate total energy: Power (W) × Time step (h) = Energy (Wh)
dt_hours = 1  # time step is 1 hour
total_energy_wh = np.sum(power) * dt_hours

# Create a new figure for plotting current vs. time
plt.figure()
# Plot current over time
plt.plot(time_hours, current)
# Label the x-axis as "Time (hours)"
plt.xlabel("Time (hours)")
# Label the y-axis as "Current (A)"
plt.ylabel("Current (A)")
# Set the title for the current plot
plt.title("Current vs Time")
# Display the current vs. time plot
plt.show()

# Create another figure for plotting power vs. time
plt.figure()
# Plot power over time
plt.plot(time_hours, power)
# Label the x-axis as "Time (hours)"
plt.xlabel("Time (hours)")
# Label the y-axis as "Power (W)"
plt.ylabel("Power (W)")
# Set the title for the power plot
plt.title("Power vs Time")
# Display the power vs. time plot
plt.show()

