#When it comes to small datasets or nearly sorted datasets, you wanna use insertion sort over other sorting algorithms
#Space complexity is O(1)
#Time complexity is O(n^2)
def insertionSort(A):
    length = len(A)
    i = 1
    while i < length:
        j = i - 1
        while A[j + 1] < A[j] and j >= 0:
            temp = A[j + 1]
            A[j + 1] = A[j]
            A[j] = temp
            j -= 1
        i += 1