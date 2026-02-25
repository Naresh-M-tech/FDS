import numpy as np

# Fuel efficiency data (miles per gallon) of different car models
fuel_efficiency = np.array([18, 22, 25, 30, 28])

# Calculate average fuel efficiency
average_efficiency = np.mean(fuel_efficiency)

# Calculate percentage improvement between Model 1 and Model 4
# (Example: 18 mpg to 30 mpg)
percentage_improvement = ((fuel_efficiency[3] - fuel_efficiency[0]) 
                          / fuel_efficiency[0]) * 100

print("Average Fuel Efficiency:", average_efficiency, "mpg")
print("Percentage Improvement:", percentage_improvement, "%")
