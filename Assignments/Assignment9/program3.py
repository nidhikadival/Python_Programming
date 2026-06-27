########################################################
##  Name : Nidhi Girish Kadival
##  Assignment 9 
##  Question 3
##  Date : 26/06/2026
########################################################

#######################################################################
##
##  Function Name : Square
##  Description :   It returns the square of the given number
##  Input :         int
##  Output :        int
##  Author :        Nidhi Girish Kadival
##  Date :          26/06/2026
## 
#######################################################################

def Square(No1):
    square = (No1*No1)

    return square


def main():
    print("Enter a number : ")
    Value = int(input())

    Result = Square(Value)

    print(Result)

if(__name__ == "__main__"):
    main()        

########################################################
##  Output:
##  Enter a number : 
##  5
##  25
##  
##  Enter a number : 
##  9
##  81
########################################################    