import matplotlib.pyplot as plt
import numpy as np

# Data for Inspirasi
time_inspirasi = np.linspace(0, 1, 1000)  # 1 second duration
frequency_inspirasi = 1  # 1 Hz
amplitude_inspirasi = 1.72 / 2  # Vpp/2 for peak amplitude
signal_inspirasi = amplitude_inspirasi * np.sin(2 * np.pi * frequency_inspirasi * time_inspirasi)

# Data for Ekspirasi
time_ekspirasi = np.linspace(0, 1, 1000)  # 1 second duration
frequency_ekspirasi = 1  # 1 Hz
amplitude_ekspirasi = 1.24 / 2  # Vpp/2 for peak amplitude
signal_ekspirasi = amplitude_ekspirasi * np.sin(2 * np.pi * frequency_ekspirasi * time_ekspirasi)

# Plotting the signals in one plot
plt.figure(figsize=(10, 6))

# Plot Inspirasi and Ekspirasi in the same plot
plt.plot(time_inspirasi, signal_inspirasi, label='Inspirasi', color='blue')
plt.plot(time_ekspirasi, signal_ekspirasi, label='Ekspirasi', color='orange')

plt.title('Sinyal Inspirasi dan Ekspirasi')
plt.xlabel('Waktu (s)')
plt.ylabel('Tegangan (V)')
plt.grid(True)
plt.legend()

plt.show()
