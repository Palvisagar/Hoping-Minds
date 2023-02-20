#  program to find factorial using recursive function
# Author Palvi Sagar

# define a function

def factorial(x):
   
    if x == 0 or x== 1:
        return 1
    else:
        # recursive call to the function
        return (x * factorial(x-1))
        
# change the value for a different result
n = 4

# call the factorial function
factorial(n)
print("The factorial of", n, "is",factorial(n))
