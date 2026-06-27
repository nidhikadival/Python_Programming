########################################################
##  Name : Nidhi Girish Kadival
##  Assignment 11
##  Question 3
##  Date : 26/06/2026
########################################################

#######################################################################
##
##  Function Name : Summation
##  Description :   It returns the addition of the digits in the no
##  Input :         int
##  Output :        int
##  Author :        Nidhi Girish Kadival
##  Date :          26/06/2026
## 
#######################################################################

def Summation(No1):
    digit = 0
    sum = 0

    while(No1 != 0):
        digit = No1%10
        sum = sum + digit
        No1 = No1//10

    return sum

def main():
    print("Enter a number : ")
    Value = int(input())

    Result = Summation(Value)

    print(Result)

if(__name__ == "__main__"):
    main()        

########################################################
##  Output:
##  Enter a number : 
##  123
##  6
##
##  Enter a number : 
##  12345
##  15
########################################################    