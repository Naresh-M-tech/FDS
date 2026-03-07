import pandas as pd
from collections import Counter
import string

reviews = [
    "This product is very good",
    "Good quality and good price",
    "Very useful product"
]

text = " ".join(reviews).lower()

# Remove punctuation
for p in string.punctuation:
    text = text.replace(p, "")

words = text.split()

frequency = Counter(words)

print("Word Frequency:")
print(frequency)
