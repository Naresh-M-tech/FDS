import pandas as pd

data = {'Likes': [10, 20, 10, 30, 20, 10, 40]}
df = pd.DataFrame(data)

frequency = df['Likes'].value_counts()

print(frequency)
