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

# Initialize lists for additional columns
xi_minus_mean = []
xi_minus_mean_sq = []
fi_xi_minus_mean_sq = []

# Calculate additional columns
for i in range(len(frequencies)):
    xi = midpoints[i]
    fi = frequencies[i]
    fixi = xi * fi
    xi_minus_mean_val = xi - mean
    xi_minus_mean_sq_val = xi_minus_mean_val ** 2
    fi_xi_minus_mean_sq_val = fi * xi_minus_mean_sq_val
    
    xi_minus_mean.append(xi_minus_mean_val)
    xi_minus_mean_sq.append(xi_minus_mean_sq_val)
    fi_xi_minus_mean_sq.append(fi_xi_minus_mean_sq_val)

# Step 4: Print frequency distribution table
print("Frequency Distribution Table")
print("----------------------------------------------------------------------------------------------------------------------------------------")
print("Class Interval      |   Frequency    |   fi    |   xi     |   fixi     |   mean     |   xi-mean     |   xi-mean^2     |   fi(xi-mean)^2")
print("----------------------------------------------------------------------------------------------------------------------------------------")
for i, interval in enumerate(class_intervals):
    interval_str = f"{interval[0]} - {interval[1]}"
    frequency_str = str(frequencies[i])
    fi_str = str(frequencies[i])
    xi_str = str(midpoints[i])
    fixi_str = str(midpoints[i] * frequencies[i])
    mean_str = str(mean)
    xi_minus_mean_str = str(xi_minus_mean[i])
    xi_minus_mean_sq_str = str(xi_minus_mean_sq[i])
    fi_xi_minus_mean_sq_str = str(fi_xi_minus_mean_sq[i])
    
    print(f"{interval_str.ljust(20)}|   {frequency_str.rjust(10)}   |   {fi_str.rjust(3)}   |   {xi_str.rjust(3)}   |   {fixi_str.rjust(6)}   |   {mean_str.rjust(6)}   |   {xi_minus_mean_str.rjust(9)}   |   {xi_minus_mean_sq_str.rjust(11)}   |   {fi_xi_minus_mean_sq_str.rjust(14)}")
print("----------------------------------------------------------------------------------------------------------------------------------------")

# Step 3: Calculate statistics
sum_fiXi = sum(midpoints[i] * frequencies[i] for i in range(len(frequencies)))
sum_fi = sum(frequencies)
mean = sum_fiXi / sum_fi

variance = (sum_fiXi2 / sum_fi) - (mean**2)

std_deviation = np.sqrt(variance)
coefficient_of_variation = (std_deviation / mean) * 100

# Step 5: Print statistics

print(f"Mean: {mean}")
print(f"Variance: {variance}")
print(f"Standard Deviation: {std_deviation}")
print(f"Coefficient of Variation: {coefficient_of_variation}")
print("\n")

# Step 6: Plot Histogram
plt.bar(midpoints, frequencies, width=25, edgecolor='black')  # Using class interval of 25
plt.title('Histogram of Grouped Data with Class Interval of 25')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.xticks(midpoints)
plt.grid(True)
plt.show()
