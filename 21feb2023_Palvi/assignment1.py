# program to  find a equiation of submmission
# Author Palvi Sagar
# created at 21_Feb_2023


# Import the math module
import math

# Define a function 
def series_sum(n):
    # Initialize the sum to 0
    sum = 0
    # Use a for loop to iterate over the values of i from 1 to n
    for i in range(1, n+1):
        # Calculate the two terms for the current value of i
        term = n / (i * math.factorial(i)) + 1 / (n * i)
        # Add the terms to the sum
        sum += term
    # Return the final sum
    return sum

# Set the value of `n` 
n = 100
# Call the function and store the result in the variable `result`
result = series_sum(n)
# Print the result 
print(result)









