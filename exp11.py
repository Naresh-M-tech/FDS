import matplotlib.pyplot as plt

months = ['Jan','Feb','Mar','Apr','May']
sales = [12000, 15000, 17000, 14000, 20000]

# 1. Line Plot
plt.plot(months, sales)
plt.title("Monthly Sales - Line Plot")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

# 2. Scatter Plot
plt.scatter(months, sales)
plt.title("Monthly Sales - Scatter Plot")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

# 3. Bar Plot
plt.bar(months, sales)
plt.title("Monthly Sales - Bar Plot")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()
