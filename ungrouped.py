import numpy as np
from statistics import median, mode, StatisticsError
import matplotlib.pyplot as plt

# Step 1: Organize the Data
data = [54, 56, 57, 60, 62, 63, 64, 65, 66, 67, 69, 70, 72, 73, 74, 74, 76, 78, 85, 88]

# Step 2: Sort the Data
sorted_data = sorted(data)
print("Sorted Data:", sorted_data)

# Step 3: Calculate Mean, Median, and Mode
mean = np.mean(data)
median = median(data)
try:
    mode_value = mode(data)
except StatisticsError:
    mode_value = "No mode found"

print("Mean:", mean)
print("Median:", median)
print("Mode:", mode_value)

# Step 4: Calculate Variance and Standard Deviation
variance = np.var(data)
std_deviation = np.std(data)

print("Variance:", variance)
print("Standard Deviation:", std_deviation)

# Step 5: Calculate Coefficient of Variation
coefficient_of_variation = (std_deviation / mean) * 100
print("Coefficient of Variation:", coefficient_of_variation)

# Step 6: Plot Histogram
plt.hist(data, bins=10, edgecolor='black')
plt.title('Histogram of Data')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
