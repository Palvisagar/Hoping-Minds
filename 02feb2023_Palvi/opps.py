#Area of Triangle by using Heron's Formula

# Author Palvi Sagar

# find area of triangle  based on sides

def areaOfTriangle(side1,side2,side3):

    # calculate semi perimeter
    s=(side1+side2+side3)/2

    #calcuate the area
    area=(s*(s-side1)*(s-side2)*(s-side3))
    print('Area of a Trinagle is %0.2f'%area)


# user inputs

side1 =float(input())
side2 =float(input())
side3 =float(input())


areaOfTriangle(side1,side2,side3)


