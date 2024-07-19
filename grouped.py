import numpy as np
import matplotlib.pyplot as plt

# Given data
data = [54, 56, 57, 60, 62, 63, 64, 65, 66, 67, 69, 70, 72, 73, 74, 74, 76, 78, 85, 88]

# Step 1: Define the specific class intervals and initialize frequencies
class_intervals = [(0, 25), (26, 50), (51, 75), (76, 100)]
frequencies = [0] * len(class_intervals)

# Populate frequencies
for value in data:
    for i, interval in enumerate(class_intervals):
        if interval[0] <= value <= interval[1]:
            frequencies[i] += 1
            break  # Break once the value is found in the interval

# Step 2: Calculate midpoints for each interval
midpoints = [(interval[0] + interval[1]) / 2 for interval in class_intervals]

# Step 3: Calculate statistics
sum_fiXi = sum(midpoints[i] * frequencies[i] for i in range(len(frequencies)))
sum_fi = sum(frequencies)
mean = sum_fiXi / sum_fi
sum_f_xi_minus_mean_sq = sum(frequencies[i] * ((midpoints[i] - mean)**2) for i in range(len(frequencies)))

# Step 4: Print frequency distribution table
print("Frequency Distribution Table")
print("----------------------------------------")
print("Class Interval      |   Frequency")
print("----------------------------------------")
for i, interval in enumerate(class_intervals):
    interval_str = f"{interval[0]} - {interval[1]}"
    frequency_str = str(frequencies[i])
    print(f"{interval_str.ljust(20)}|   {frequency_str.rjust(10)}")
print("----------------------------------------")

# Step 5: Print statistics
print(f"Sum of frequency: {sum_fi}")
print(f"Sum of frequency and midpoint: {sum_fiXi}")
print(f"Mean: {mean}")
print(f"\nΣ f(x_i - mean)^2: {sum_f_xi_minus_mean_sq}") 

# Step 6: Calculate variance and continue with existing code
variance = (sum_f_xi_minus_mean_sq / sum_fi)
std_deviation = np.sqrt(variance)
coefficient_of_variation = (std_deviation / mean) * 100

print(f"Variance: {variance}")
print(f"Standard Deviation: {std_deviation}")
print(f"Coefficient of Variation: {coefficient_of_variation}")
print("\n")

# Step 7: Plot Histogram
plt.bar(midpoints, frequencies, width=25, edgecolor='black')  # Using class interval of 25
plt.title('Histogram of Grouped Data with Class Interval of 25')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.xticks(midpoints)
plt.grid(True)
plt.show()
