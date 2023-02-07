# call the inner function from in the nested function
# Autor Palvi Sagar

def mainFun():   # outer function
    s="This is a main function"

    def innerFun(): # inner function
        print("This is the inner function") # print inner function
        print(s)   # print outer function in inner function

    innerFun() #inner function end

mainFun(); # outer function end 
        