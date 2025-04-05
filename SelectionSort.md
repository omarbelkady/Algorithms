```plaintext
function SelectionSort(array):
    n = length(array)
    for i from 0 to n-1:
        minIndex = i
        for j from i+1 to n-1:
            if array[j] < array[minIndex]:
                minIndex = j
        swap(array[i], array[minIndex])
```