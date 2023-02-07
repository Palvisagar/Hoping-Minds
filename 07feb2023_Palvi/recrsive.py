#  program to find factorial
# Author Palvi Sagar

# define a function

n = 5
def factorial(n):
	#  find factorial
   if n == 1 or n == 0:
      return 1
   else :
     factorial(n - 1)

# call the function

print("Factorial of",n,"is",factorial(n))

