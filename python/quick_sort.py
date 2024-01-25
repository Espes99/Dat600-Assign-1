#Quick sort using comprehension
#ref: https://www.geeksforgeeks.org/python-program-for-quicksort/
def quick_sort(arr):
    # This function sorts the array and returns the number of steps
    if len(arr) <= 1:
        return 0

    pivot = arr[0]
    left = []
    right = []
    steps = 0

    for x in arr[1:]:
        steps += 1  # for comparison
        if x < pivot:
            left.append(x)
        else:
            right.append(x)

    steps_left = quick_sort(left)  # Recursively sort left part
    steps_right = quick_sort(right)  # Recursively sort right part
    
    return steps + steps_left + steps_right
