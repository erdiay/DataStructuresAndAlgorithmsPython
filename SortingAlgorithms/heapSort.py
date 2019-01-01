import math

#Space complexity is O(1)
#Time complexity is O(nlgn)
#The most direct competitor of quick sort. Quick sort is usually more faster, though there remains the chance of
#worst case performance
#Note that this is not a stable sorting algorithm
def heapSort(A):
    heap_size = len(A)
    __build_heap(A)
    #print A #uncomment this print to see the heap it builds
    for i in range(heap_size-1,0,-1):
        A[0], A[i] = A[i], A[0]
        heap_size -= 1
        __max_heapify(A, heap_size, 0)

def __max_heapify(A, heap_size, i):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    if left < heap_size and A[left] > A[largest]:
        largest = left
    if right < heap_size and A[right] > A[largest]:
        largest = right
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        __max_heapify(A, heap_size, largest)

def __build_heap(A):
    heap_size = len(A)
    for i in range (math.floor(heap_size/2),-1,-1):
        __max_heapify(A,heap_size, i)

