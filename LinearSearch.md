function LinearSearch(array, target):
    for i from 0 to length(array)-1:
        if array[i] == target:
            return i
    return -1