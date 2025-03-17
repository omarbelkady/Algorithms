```plaintext
function QuickSort(array, low, high):
    if low < high:
        pivotIndex = Partition(array, low, high)
        QuickSort(array, low, pivotIndex-1)
        QuickSort(array, pivotIndex+1, high)

function Partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j from low to high-1:
        if array[j] <= pivot:
            i = i + 1
            swap(array[i], array[j])
    swap(array[i+1], array[high])
    return i+1
```