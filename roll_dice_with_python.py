import random
from collections import Counter

x = []

for j in range(100):
    num = random.randint(1, 6)
    x.append(num)

counts = Counter(x)

print(counts)

# Execute the code and you will see that out of 100 rolls, you get more or less same distribution of numbers. Probability!!
