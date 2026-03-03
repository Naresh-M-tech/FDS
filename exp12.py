import matplotlib.pyplot as plt

months = ['Jan','Feb','Mar','Apr','May']
temperature = [22, 25, 30, 35, 33]
rainfall = [10, 20, 15, 5, 8]

# Line Plot (Temperature)
plt.plot(months, temperature)
plt.title("Monthly Temperature")
plt.xlabel("Month")
plt.ylabel("Temperature (°C)")
plt.show()

# Scatter Plot (Rainfall)
plt.scatter(months, rainfall)
plt.title("Monthly Rainfall")
plt.xlabel("Month")
plt.ylabel("Rainfall (mm)")
plt.show()
