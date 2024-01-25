#ref: course module - Coding sessions
def insertion_sort(arr):
    #Implement insertion sort algorithm
    steps=0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        steps+=2
        while j >= 0 and arr[j] > key:
            #Shift elements to the right
            arr[j+1] = arr[j]
            j -= 1
            steps+=2
        arr[j+1] = key
        steps+=1
    return steps
