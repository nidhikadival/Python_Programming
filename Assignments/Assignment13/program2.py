########################################################
##  Name : Nidhi Girish Kadival
##  Assignment 13
##  Question 2
##  Date : 26/06/2026
########################################################

#######################################################################
##
##  Function Name : Area
##  Description :   It prints the area of the rectangle
##  Input :         int
##  Output :        int
##  Author :        Nidhi Girish Kadival
##  Date :          26/06/2026
## 
#######################################################################

def AreaCircle(Radius):
    pi = 3.14
    area = pi * (Radius * Radius)
    return area

def main():
    print("Enter the radius of the circle : ")
    radius = int(input())

    area = AreaCircle(radius)

    print("Area of circle is : ",area)

if(__name__ == "__main__"):
    main()        

########################################################
##  Output:
##  Enter the radius of the circle : 
##  30
##  Area of circle is :  2826.0
##
##  Enter the radius of the circle : 
##  25
##  Area of circle is :  1962.5 
########################################################    