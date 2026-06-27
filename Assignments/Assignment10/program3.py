########################################################
##  Name : Nidhi Girish Kadival
##  Assignment 10
##  Question 3
##  Date : 26/06/2026
########################################################

#######################################################################
##
##  Function Name : Factorial
##  Description :   It returns the factorial of the given number
##  Input :         int
##  Output :        int
##  Author :        Nidhi Girish Kadival
##  Date :          26/06/2026
## 
#######################################################################

def Factorial(No):
    fact = 1

    for i in range(1,(No+1)):
        fact = fact * i

    return fact   

def main():
    print("Enter a number :")
    Value = int(input())

    Result = Factorial(Value)

    print(Result)

if(__name__ == "__main__"):
    main()    

########################################################
##  Output:
##  Enter a number :
##  5
##  120
##
##  Enter a number :
##  4
##  24   
########################################################
