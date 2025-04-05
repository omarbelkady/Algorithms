```plaintext
function KMP(text, pattern):
    lps = ComputeLPS(pattern)
    i = 0, j = 0
    while i < length(text):
        if text[i] == pattern[j]:
            i++, j++
            if j == length(pattern):
                return i - j
        else:
            if j != 0:
                j = lps[j-1]
            else:
                i++
    return -1
```
```plaintext
function ComputeLPS(pattern):
    lps = [0] * length(pattern)
    len = 0, i = 1
    while i < length(pattern):
        if pattern[i] == pattern[len]:
            len++, lps[i] = len, i++
        else:
            if len != 0:
                len = lps[len-1]
            else:
                lps[i] = 0, i++
    return lps
```
