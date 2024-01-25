#Quick sort using comprehension
#ref: https://www.geeksforgeeks.org/python-program-for-quicksort/
def quick_sort(arr):
    steps = 0
    if len(arr) <= 1:
        return steps
    else:
        pivot = arr[0]
        left = []
        right = []
        steps += 1  

        for x in arr[1:]:
            steps += 1 
            if x < pivot:
                left.append(x)
            else:
                right.append(x)


        steps += quick_sort(left)
        steps += quick_sort(right)


        steps += len(left) + len(right) + 1
        
        return steps
