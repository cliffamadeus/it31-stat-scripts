import numpy as np
import matplotlib.pyplot as plt

# Given data
data = [54, 56, 57, 60, 62, 63, 64, 65, 66, 67, 69, 70, 72, 73, 74, 79, 76, 78, 85, 88]

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
midpoints = [(low + high) / 2 for low, high in class_intervals]

# Step 3: Calculate statistics
sum_fi = sum(frequencies)
sum_fiXi = sum(midpoint * frequency for midpoint, frequency in zip(midpoints, frequencies))
mean = sum_fiXi / sum_fi

# Step 4: Print frequency distribution table and calculate statistics
print("Frequency Distribution Table")
print("-----------------------------------------------------------------------------------------------------")
print("Class Interval      | Frequency(f) | Midpoint(Xi) |    f*Xi     |  xi-mean   | (xi-mean)^2  | f(xi-mean)^2")
print("-----------------------------------------------------------------------------------------------------")

sum_fximean2 = 0
sum_fXi = 0

for (low, high), frequency, midpoint in zip(class_intervals, frequencies, midpoints):
    interval_str = f"{low} - {high}"
    fXi = frequency * midpoint
    xi_minus_mean = midpoint - mean
    xi_minus_mean2 = xi_minus_mean ** 2
    f_xi_minus_mean2 = frequency * xi_minus_mean2
    sum_fximean2 += f_xi_minus_mean2
    sum_fXi += fXi
    
    print(f"{interval_str.ljust(20)}|{str(frequency).rjust(13)}|{midpoint:12.3f}|{fXi:12.3f}|{xi_minus_mean:12.3f}|{xi_minus_mean2:14.3f}|{f_xi_minus_mean2:18.3f}")

print("-----------------------------------------------------------------------------------------------------")
print(f"Total               |{str(sum_fi).rjust(13)}|{str().rjust(12)}|{sum_fXi:12.3f}|{str().rjust(12)}|{str().rjust(14)}|{sum_fximean2:18.3f}")



# Step 5: Print statistics
print(f"\nSum of frequency: {sum_fi}")
print(f"Sum of frequency and midpoint: {sum_fiXi}")
print(f"Mean: {mean}")
print(f"\nΣ f(x_i - mean)^2: {sum_fximean2}")

# Step 6: Calculate variance and continue with existing code
variance = (sum_fximean2 / sum_fi)
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
