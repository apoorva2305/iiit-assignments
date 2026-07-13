#fibonacci numbers
def fibonacci_series(n):
    # Initialize the first two terms
    a, b = 0, 1
    
    # Generate the series
    for _ in range(n):
        print(a, end=" ")
        # Swap values: next term is the sum of previous two
        a, b = b, a + b

# Example: Generate the first 10 numbers
terms = 10
print(f"Fibonacci series ({terms} terms):")
fibonacci_series(terms)
