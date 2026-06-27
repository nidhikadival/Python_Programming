########################################################
##  Name : Nidhi Girish Kadival
##  Assignment 10
##  Question 2
##  Date : 26/06/2026
########################################################

#######################################################################
##
##  Function Name : Summation
##  Description :   It returns the addition of N natural numbers 
##  Input :         int
##  Output :        int
##  Author :        Nidhi Girish Kadival
##  Date :          26/06/2026
## 
#######################################################################

def Summation(No):
    sum = 0

    for i in range(1,(No+1)):
        sum = sum + i

    return sum   

def main():
    print("Enter a number :")
    Value = int(input())

    Result = Summation(Value)

    print(Result)

if(__name__ == "__main__"):
    main()    

########################################################
##  Output:
##  Enter a number :
##  5
##  15
##
##  Enter a number :
##  10
##  55    
########################################################
