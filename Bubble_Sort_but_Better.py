import random
from tqdm import tqdm
import time

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

array = random.choices(range(1, 450), k=450)

for i in tqdm(range(len(array))):
    bubble_sort(array)

    # A little bit delay to visualize the progression
    time.sleep(0.01)

print(array)
