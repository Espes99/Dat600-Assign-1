#ref: https://www.geeksforgeeks.org/python-program-for-heap-sort/
#Added steps to the heap sort function
def heap_sort(arr):
    steps = 0
    n = len(arr)
    steps += 1  # Counting the initialization of n

    for i in range(n, -1, -1):
        steps += heapify(arr, n, i)  # Include steps from heapify
        steps += 1  # For the iteration step

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap
        steps += 1  # For the swap
        steps += heapify(arr, i, 0)  # Include steps from heapify
        steps += 1  # For the iteration step

    return steps

def heapify(arr, n, i):
    steps = 0
    largest = i  
    l = 2 * i + 1
    r = 2 * i + 2

    steps += 3  

    if l < n and arr[i] < arr[l]:
        largest = l
        steps += 1 

    if r < n and arr[largest] < arr[r]:
        largest = r
        steps += 1 

    if largest != i:
        (arr[i], arr[largest]) = (arr[largest], arr[i])
        steps += 1  # For the swap
        steps += heapify(arr, n, largest) 

    return steps
