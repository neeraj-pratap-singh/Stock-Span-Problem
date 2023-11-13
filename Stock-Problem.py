# Task 1
# start by intilizing the necessary variables such as n to store the length of price array , span as an array of zeros to store the stock span, and set the span of first day to 1 

# Task 2: Transverse through the prices
# Iterate through the prices array from the second to the last day

def calculate_stock_span(prices):
    # Length of the prices array
    n = len(prices)

    # Initialize the span array with zeros
    span = [0] * n

    # Set the span for the first day to 1
    span[0] = 1

    # Iterate through the prices array from the second day
    for i in range(1, n):
        span[i] = 1  # Initialize span for the current day

        # Traverse back to previous days to check how many days' prices were less than or equal to the current day's price
        j = i - 1
        while j >= 0 and prices[j] <= prices[i]:
            span[i] += 1
            j -= 1

    return span

# Example usage
prices = [100, 80, 60, 70, 60, 75, 85]
print("Stock spans:", calculate_stock_span(prices))
