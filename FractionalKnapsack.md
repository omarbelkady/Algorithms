function FractionalKnapsack(weights, values, capacity):
    items = [(values[i]/weights[i], weights[i]) for i in range(length(weights))]
    sort items by value-to-weight ratio descending
    totalValue = 0
    for ratio, weight in items:
        if capacity >= weight:
            totalValue += ratio * weight
            capacity -= weight
        else:
            totalValue += ratio * capacity
            break
    return totalValue