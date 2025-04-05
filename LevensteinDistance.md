```plaintext
function EditDistance(word1, word2):
    m = length(word1)
    n = length(word2)
    dp = [[0] * (n+1) for _ in range(m+1)]
    for i from 0 to m:
        dp[i][0] = i
    for j from 0 to n:
        dp[0][j] = j
    for i from 1 to m:
        for j from 1 to n:
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    return dp[m][n]
```