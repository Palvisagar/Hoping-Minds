def InsertionSort(a):
  
    # traversing the array from 1 to length of the array(a)
    for i in range(1, len(a)):
  
        temp = a[i]
  
        # Shift elements of array[0 to i-1], that are greater than temp, to one position ahead
        # of their current position
        j = i-1
        while j >=0 and temp < a[j] :
                a[j+1] = a[j]
                j -= 1
        a[j+1] = temp

def InsertionSort(b):
  
    # traversing the array from 1 to length of the array(b)
    for i in range(1, len(b)):
  
        temp = b[i]
  
        # Shift elements of array[0 to i-1], that are smaller than temp, to one position ahead
        # of their current position
        j = i-1
        while j >=0 and temp > b[j] :
                b[j+1] = b[j]
                j -= 1
        b[j+1] = temp

# array to be sorted        
a = [10, 5, 13, 8, 2]
b = [2, 5, 7, 8, 10]

InsertionSort(a)
InsertionSort(b)


print("Array after sorting:")
print(a)
print(b)



