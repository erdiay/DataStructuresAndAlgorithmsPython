#Space complexity is O(1)
#Time complexity is O(n^2)
def selectionSort(A):
    length = len(A)
    i = 0
    while i < length:
        min = A[i]
        minIndex = i
        j = i + 1
        while j < length:
            if A[j] < min:
                min = A[j]
                minIndex = j
            j += 1
        temp = A[i]
        A[i] = min
        A[minIndex] = temp
        i += 1
