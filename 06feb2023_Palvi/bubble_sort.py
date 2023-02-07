# program bubble sort
# Author Palvi Sagar

# define a function for accending order

def bubleSort(array):
    swapFlag = True

    #define a loop

    while swapFlag:
        swapFlag= False

        # range of i and repeat the loop

        for i in range(len(array)-1):

            # compare the elements and swapped

            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                
                # print the swapped elements

                print("Swapped: {} with {}".format(array[i], array[i+1]))
                swapFlag = True
    return array
arr = [5,4,3,2,1,6,7,8,9,10]
#call the function
print(bubleSort(arr))

# end function of accending order


# define a function for desending order

def bubleSort(array):
    swapFlag = True

    #define a loop

    while swapFlag:
        swapFlag= False

        # range of i and repeat the loop

        for i in range(len(array)-1):

             # compare the elements and swapped

            if array[i] < array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                
                # print the swapped elements

                print("Swapped: {} with {}".format(array[i], array[i+1]))
                swapFlag = True
    return array
arr = [5,4,3,2,1,6,7,8,9,10]

#call the function
print(bubleSort(arr))

# end function of desending order


