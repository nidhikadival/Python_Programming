########################################################
##  Name : Nidhi Girish Kadival
##  Assignment 11
##  Question 2
##  Date : 26/06/2026
########################################################

#######################################################################
##
##  Function Name : Digits
##  Description :   It returns the no of digits in a number
##  Input :         int
##  Output :        int
##  Author :        Nidhi Girish Kadival
##  Date :          26/06/2026
## 
#######################################################################

def Digits(No1):
    digits = 0

    if(No1 == 0):
        return 1

    while(No1 != 0):
        digits = digits + 1
        No1 = No1//10

    return digits

def main():
    print("Enter a number : ")
    Value = int(input())

    Result = Digits(Value)

    print(Result)

if(__name__ == "__main__"):
    main()        

########################################################
##  Output:
##  Enter a number : 
##  0
##  1
##
##  Enter a number : 
##  3456
##  4
##
##  Enter a number : 
##  778
##  3
########################################################    