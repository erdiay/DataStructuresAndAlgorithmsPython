from SortingAlgorithms.bubbleSort import bubbleSort
from SortingAlgorithms.selectionSort import selectionSort
from SortingAlgorithms.insertionSort import insertionSort
from SortingAlgorithms.mergeSort import mergeSort
from SortingAlgorithms.quickSort import quickSort
from SortingAlgorithms.heapSort import heapSort

sortedArray = [0, 1, 2, 4, 5, 6, 44, 63, 87, 99, 283]

def bubbleSortTest():
    A = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
    bubbleSort(A)

    assert A == sortedArray 

    print("Sorted array: ")
    print()
    for i in A:
        print(i, end=" ") 

def selectionSortTest():
    A = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
    selectionSort(A)
    
    assert A == sortedArray 

    print("Sorted array: ")
    print()
    for i in A:
        print(i, end=" ") 

def insertionSortTest():
    A = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
    insertionSort(A)
    
    assert A == sortedArray 

    print("Sorted array: ")
    print()
    for i in A:
        print(i, end=" ") 

def mergeSortTest():
    A = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
    mergeSort(A)
    
    assert A == sortedArray 

    print("Sorted array: ")
    print()
    for i in A:
        print(i, end=" ") 

def quickSortTest():
    A = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
    #A = [99, 11, 12, 1]
    quickSort(A)
    
    assert A == sortedArray 

    print("Sorted array: ")
    print()
    for i in A:
        print(i, end=" ") 

def heapSortTest():
    #A = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
    A = [10, 14, 9, 7, 8, 5]
    heapSort(A)
    
    assert A == sortedArray 

    print("Sorted array: ")
    print()
    for i in A:
        print(i, end=" ") 

#bubbleSortTest()
#selectionSortTest()
#insertionSortTest()
#mergeSortTest()
#quickSortTest()
heapSortTest()