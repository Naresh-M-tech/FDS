from collections import Counter
import string

# Read file
with open("pr.txt", "r") as file:
    text = file.read().lower()

# Remove punctuation
for p in string.punctuation:
    text = text.replace(p, "")

words = text.split()

frequency = Counter(words)

print(frequency)
