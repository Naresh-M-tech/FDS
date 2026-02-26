import matplotlib.pyplot as plt

months = ['Jan','Feb','Mar','Apr','May']
sales = [10000, 15000, 12000, 18000, 20000]

# Line Plot
plt.plot(months, sales)
plt.title("Monthly Sales - Line Plot")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

# Bar Plot
plt.bar(months, sales)
plt.title("Monthly Sales - Bar Plot")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()
