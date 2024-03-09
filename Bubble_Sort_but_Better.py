import random
from tqdm import tqdm
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

array = random.choices(range(1, 1000), k=1000)

for i in tqdm(range(len(array))):
    bubble_sort(array)

    # A Little bit delay to visualize the progression
    time.sleep(0.01)

print(array[:10])
