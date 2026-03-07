import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt

data = pd.DataFrame({
'feedback':[
"good service",
"very good product",
"bad service",
"good quality",
"excellent product"
]
})

text = " ".join(data['feedback']).lower()
words = text.split()

freq = Counter(words)

top_words = dict(freq.most_common(5))

print("Top Words:", top_words)

plt.bar(top_words.keys(), top_words.values())
plt.title("Top Frequent Words")
plt.show()
