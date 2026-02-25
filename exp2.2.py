import matplotlib.pyplot as plt
# Months of the year
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
"Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
# Monthly rainfall data (in mm)
rainfall = [20, 25, 30, 40, 60, 120, 150, 140, 90, 60, 35, 25]
# Scatter plot
plt.figure()
plt.scatter(months, rainfall)
plt.xlabel("Months")
plt.ylabel("Rainfall (mm)")
plt.title("Monthly Rainfall Data")
plt.show()
