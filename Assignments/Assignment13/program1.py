########################################################
##  Name : Nidhi Girish Kadival
##  Assignment 13
##  Question 1
##  Date : 26/06/2026
########################################################

#######################################################################
##
##  Function Name : Area
##  Description :   It prints the area of the rectangle
##  Input :         int, int
##  Output :        int
##  Author :        Nidhi Girish Kadival
##  Date :          26/06/2026
## 
#######################################################################

def Area(Length,Width):
    area = Length * Width
    return area

def main():
    print("Enter a length : ")
    Length = int(input())

    print("Enter a width : ")
    Width = int(input())

    area = Area(Length,Width)

    print("Area of rectangle is : ",area)

if(__name__ == "__main__"):
    main()        

########################################################
##  Output:
##  Enter a length : 
##  15
##  Enter a width : 
##  4
##  Area of rectangle is :  60
##
##  Enter a length : 
##  20
##  Enter a width : 
##  40
##  Area of rectangle is :  800  
########################################################    