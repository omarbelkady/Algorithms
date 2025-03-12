function BinarySearch(array, target):
    
low = 0

high = length(array) - 1

while low <= high:
    mid = (low + high) / 2
    if array[mid] == target:
        return mid
    elif array[mid] < target:
        low = mid + 1
    else:
        high = mid - 1
return -1
