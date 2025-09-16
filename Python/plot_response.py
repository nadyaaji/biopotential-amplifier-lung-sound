import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Data from the image
frequencies = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500, 10000]
gains = [-30, -30, -30, -28, -28, -26, -26, -26, -25, -25, -21, -16, -13, -10, -7, -6, -4, -3, -3, 1, 2, 2, 2, 2, 2, 1, 1, 1, -1, -3, -5, -7, -9, -11, -12, -14, -16, -16, -17, -17, -20, -20, -20, -21, -22, -24]

# Convert frequencies and gains to numpy arrays
frequencies = np.array(frequencies)
gains = np.array(gains)

# Interpolating to get a smooth curve
xnew = np.logspace(np.log10(frequencies.min()), np.log10(frequencies.max()), 400)
spl = make_interp_spline(frequencies, gains, k=3)  # BSpline object
gains_smooth = spl(xnew)

# Create the Bode plot
plt.figure(figsize=(10, 6))

# Plot Gain vs Frequency
plt.semilogx(frequencies, gains, 'o')
plt.semilogx(xnew, gains_smooth)

# Add vertical lines for cutoff frequencies at 80 Hz and 2000 Hz
plt.axvline(x=80, color='red', linestyle='--')
plt.axvline(x=2000, color='green', linestyle='--')

# Add grid, labels, and title
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Gain (dB)')
plt.legend()

# Show the plot
plt.show()
