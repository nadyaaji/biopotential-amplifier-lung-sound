import numpy as np

data = [152, 64, 72, 48, 56, 40, 136, 64, 56, 58, 80, 192, 56, 88, 72, 112, 56, 80, 40]

# Menghitung rata-rata
mean = np.mean(data)

# Menghitung standar deviasi
standard_deviation = np.std(data)

print("Mean (Rata-rata):", mean)
print("Standard Deviation (Standar Deviasi):", standard_deviation)
