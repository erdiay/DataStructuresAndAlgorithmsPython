import random

def quickSort(A):
    __quickSort(A, 0, len(A) - 1)

def __quickSort(A, low, high):
    if low < high:
        partitionIndex = __partition(A, low, high)
        __quickSort(A, low, partitionIndex - 1)
        __quickSort(A, partitionIndex + 1, high)

def __partition(A, low, high):
    pivot = A[high]
    i = j = low
    while j < high:
        if A[j] < pivot:
            if i != j:
                temp = A[j]
                A[j] = A[i]
                A[i] = temp
            i += 1
        j += 1
    temp = A[high]
    A[high] = A[i]
    A[i] = temp

    return i
    
    
    


