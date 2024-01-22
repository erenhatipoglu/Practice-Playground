#%%
arr = [3,5,1,9,5,7,3,4]
#%%
### 1. Display the array

def display(x):
    return print(x)

display(arr)
# %%
### 2. Add a number at the end

def add_end(x,y):
    return x.append(y)
add_end(arr, 100)

display(arr)
#%%
### 3. Add a number at the beginning

def add_beg(arr, num):
    arr.insert(0,num)

add_beg(arr, 30000)
arr
# %%
### 4. Add a number to somewhere

def add_somewhere(arr,index,num):
    for i, a in enumerate(arr):
        if i == index:
            arr.insert(i, num)
            return

add_somewhere(arr,4,-999)
arr
#%%
### 5. Delete number from the index

def delete(arr, index):
    for i, a in enumerate(arr):
        if i == index:
            arr.pop(i)
            return
        
delete(arr, 2)
arr        
#%%
### 6.Search the number

def search(arr, num):
    indices = [i for i, x in enumerate(arr) if x == num]
    if indices:
        return print("Number", num, "found at indices:", indices)
    else:
        return print("Number", num, "not found")
        
search(arr, 4)
search(arr, -100)
# %%
### 7. Get the number from the index

def get(arr, index):
    for i, a in enumerate(arr):
        if i == index:
            return a
    return -1

get(arr, 0)
# %%
### 8.Set the number to another, by index

def replace(arr, index, num):
    if index not in range(len(arr)):
        return print("index out of range")

    for i, a in enumerate(arr):
        if i == index:
            arr[index] = num
            return arr

replace(arr, 5214, -100000000)
replace(arr, 1, 200)

# %%
### 9. Max/Min finder

def minmax_finder(arr):
    minval = maxval = arr[0]
    for i in arr:
        if i < minval:
            minval = i
        elif i > maxval:
            maxval = i
            
    return ("min:",minval, "max:",maxval)

minmax_finder(arr)
# %%
### 10. Reverse the arr

def reversed(arr):
    for n in range(len(arr)):
        for i in range(len(arr) // 2):
            arr[i], arr[len(arr) - 1 - i] = arr[len(arr) - 1 - i], arr[i]
        return arr

reversed(arr)
# %%
### 11. Rotate that arr

def rotate(arr, rot):
    n = len(arr)
    arr[:] = arr[rot:n] + arr[0:rot]
    return arr

rotate(arr, 1)
