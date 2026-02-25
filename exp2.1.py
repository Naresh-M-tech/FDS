import matplotlib.pyplot as plt

# Months of the year
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
"Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
# Monthly temperature data (in °C)
temperature = [22, 24, 28, 32, 35, 34, 31, 30, 29, 27, 25, 23]
# Line plot
plt.figure()
plt.plot(months, temperature)
plt.xlabel("Months")
plt.ylabel("Temperature (°C)")
plt.title("Monthly Temperature Data")
plt.show()
