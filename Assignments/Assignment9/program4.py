########################################################
##  Name : Nidhi Girish Kadival
##  Assignment 9 
##  Question 4
##  Date : 26/06/2026
########################################################

#######################################################################
##
##  Function Name : Cube
##  Description :   It returns the cube of the given number
##  Input :         int
##  Output :        int
##  Author :        Nidhi Girish Kadival
##  Date :          26/06/2026
## 
#######################################################################

def Cube(No1):
    cube = (No1*No1*No1)

    return cube


def main():
    print("Enter a number : ")
    Value = int(input())

    Result = Cube(Value)

    print(Result)

if(__name__ == "__main__"):
    main()        

########################################################
##  Output:
##  Enter a number : 
##  4
##  64
##
##  Enter a number : 
##  5
##  125
########################################################    