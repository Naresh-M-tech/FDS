import pandas as pd
import matplotlib.pyplot as plt

data = {
'Age':[23,25,30,35,40],
'Fat':[15,18,20,22,25]
}

df = pd.DataFrame(data)

print("Mean:\n", df.mean())
print("Median:\n", df.median())
print("Standard Deviation:\n", df.std())

# Boxplot
df.boxplot()
plt.show()

# Scatter Plot
plt.scatter(df['Age'], df['Fat'])
plt.xlabel("Age")
plt.ylabel("%Fat")
plt.show()
