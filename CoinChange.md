function LIS(array):
    n = length(array)
    dp = [1] * n
    for i from 1 to n-1:
        for j from 0 to i-1:
            if array[j] < array[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)