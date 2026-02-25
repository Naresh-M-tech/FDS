import numpy as np

# Sample house data
# Columns: Bedrooms, Square Footage, Sale Price
house_data = np.array([
    [3, 1500, 250000],
    [5, 2000, 400000],
    [4, 1800, 300000],
    [6, 2500, 500000],
    [2, 1200, 200000]
])

# Filter houses with more than 4 bedrooms
filtered_houses = house_data[house_data[:, 0] > 4]

# Calculate average sale price
average_price = np.mean(filtered_houses[:, 2])

print("Average Sale Price of houses with more than 4 bedrooms:", average_price)
