'''plaintext

function Knapsack(weights, values, capacity):
    n = length(weights)
    dp = [[0] * (capacity+1) for _ in range(n+1)]
    for i from 1 to n:
        for w from 0 to capacity:
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + values[i-1])
            else:
                dp[i][w] = dp[i-1][w]
    return dp[n][capacity]
'''