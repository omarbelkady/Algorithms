function MergeSort(array):
    if length(array) <= 1:
        return array
    mid = length(array) / 2
    left = MergeSort(array[0:mid])
    right = MergeSort(array[mid:])
    return Merge(left, right)

function Merge(left, right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            append(left[0] to result)
            remove(left[0])
        else:
            append(right[0] to result)
            remove(right[0])
    append remaining elements of left and right to result
    return result