import pandas as pd

data = {'Age': [22, 25, 22, 30, 25, 30, 30]}
df = pd.DataFrame(data)

frequency = df['Age'].value_counts()

print(frequency)
