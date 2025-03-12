function BubbleSort(array):
    n = length(array)
    for i from 0 to n-1:
        for j from 0 to n-i-2:
            if array[j] > array[j+1]:
                swap(array[j], array[j+1])