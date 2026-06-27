########################################################
##  Name : Nidhi Girish Kadival
##  Assignment 12
##  Question 3
##  Date : 26/06/2026
########################################################

###############################################################################################
##
##  Function Name : Calculation
##  Description :   It returns the addition,subtraction,multiplication & division of 2 numbers
##  Input :         int
##  Output :        int,int,int,float
##  Author :        Nidhi Girish Kadival
##  Date :          26/06/2026
## 
###############################################################################################

def Calulation(No1,No2):
    sum = No1 + No2
    sub = No1 - No2
    prod = No1 * No2
    div = No1 / No2

    return sum,sub,prod,div

def main():
    print("Enter first number : ")
    Value1 = int(input())

    print("Enter second number : ")
    Value2 = int(input())

    Ret1,Ret2,Ret3,Ret4 = Calulation(Value1,Value2)

    print("Addition is ",Ret1)
    print("Substraction is ",Ret2)
    print("Multiplication is ",Ret3)
    print("Division is ",Ret4)

if(__name__ == "__main__"):
    main()        

########################################################
##  Output:
##  Enter first number : 
##  12
##  Enter second number : 
##  4
##  Addition is  16
##  Substraction is  8
##  Multiplication is  48
##  Division is  3.0   
########################################################    