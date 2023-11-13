# Task 1
# start by intilizing the necessary variables such as n to store the length of price array , span as an array of zeros to store the stock span, and set the span of first day to 1 
def calculate_stock_span(prices):
    # Length of the prices array
    n = len(prices)

    # Initialize the span array with zeros
    span = [0] * n

    # Set the span for the first day to 1
    span[0] = 1

    # Rest of the implementation will go here

    return span

# Example usage
prices = [100, 80, 60, 70, 60, 75, 85]
print("Stock spans:", calculate_stock_span(prices))
