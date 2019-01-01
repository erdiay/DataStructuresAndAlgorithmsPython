#Space complexity is O(1)
#Time complexity is O(n^2)
def bubbleSort(input):
    length = len(input)
    i = j = 0
    while i < length:
        while j < length - 1:
            if input[j + 1] < input[j]:
                temp = input[j + 1]
                input[j + 1] = input[j]
                input[j] = temp
            j += 1
        j = 0
        i += 1
