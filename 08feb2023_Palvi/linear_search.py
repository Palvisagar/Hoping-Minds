# program of searching
# Author Palvi Sagar
# created at 08-02-23

# define the function 
def linearSearch(array, n, x):

    # Going through array sequencially by using loop
    for i in range(0, n):

        #define the condition  to find the element
        if (array[i] == x):
            return i
    return -1

# search sapce
array = [5,4,3,2,1,6,7,8,9,10]

# user enter that element if find
x = int(input("enter the element"))
n = len(array)

# call the function
result = linearSearch(array, n, x)

# define the statement element is their or not
if(result == -1):
    print(x,"is not found") 
else:
    print(x,"is found at index", result)

