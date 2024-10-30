def knapsack(weights, values, capacity):
    # Number of items
    n = len(values)
    
    # Create a 2D DP array to store the maximum value for each weight limit
    dp = [[0 for x in range(capacity + 1)] for y in range(n + 1)]
    
    # Fill the DP array
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])
            else:
                dp[i][w] = dp[i - 1][w]
    
    # The maximum value will be at dp[n][capacity]
    return dp[n][capacity]

# Example usage
weights = [2, 3, 4, 5]  # weights of items
values = [3, 4, 5, 6]   # values of items
capacity = 5            # maximum capacity of the knapsack

max_value = knapsack(weights, values, capacity)
print("Maximum value in Knapsack =", max_value)
