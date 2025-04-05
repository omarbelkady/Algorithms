```plaintext
FUNCTION binary_search(array, target):
    SET low = 0                  
    SET high = LENGTH(array) - 1
    WHILE low <= high:           # Level 1
        SET mid = FLOOR((low + high) / 2)  
        IF array[mid] == target:           # Level 2
            RETURN mid                     # Level 3
        ELSE IF array[mid] < target:       # Level 2
            SET low = mid + 1              # Level 3
        ELSE:                              # Level 2
            SET high = mid - 1             # Level 3
        END IF                             # Level 2
    END WHILE                              # Level 1
    RETURN -1                              # Level 1
END FUNCTION
```
