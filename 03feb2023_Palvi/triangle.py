# # Pascal's Triangle
# #author Palvi sagar



# define a function
def solve(n):
   for i in range(n+1): # define a loop
      for j in range(n-i):
         print(' ', end='')

      C = 1
      for j in range(1, i+1):
         print(C, ' ', sep='', end='') # start to create a triangle
         C = C * (i - j) // j
      print()

n = 5
solve(n)