function RabinKarp(text, pattern):
    prime = 101
    d = 256
    h = d^(length(pattern)-1) % prime
    pHash = tHash = 0
    for i from 0 to length(pattern)-1:
        pHash = (d * pHash + pattern[i]) % prime
        tHash = (d * tHash + text[i]) % prime
    for i from 0 to length(text)-length(pattern):
        if pHash == tHash and text[i:i+length(pattern)] == pattern:
            return i
        if i < length(text)-length(pattern):
            tHash = (d * (tHash - text[i] * h) + text[i+length(pattern)]) % prime
            if tHash < 0:
                tHash += prime
    return -1