########################################################
##  Name : Nidhi Girish Kadival
##  Assignment 11
##  Question 4
##  Date : 26/06/2026
########################################################

#######################################################################
##
##  Function Name : ReverseNo
##  Description :   It returns the reverse of the given number
##  Input :         int
##  Output :        int
##  Author :        Nidhi Girish Kadival
##  Date :          26/06/2026
## 
#######################################################################

def ReverseNo(No1):
    reverse = 0

    while(No1 != 0):
        digit = No1%10
        reverse = reverse*10 + digit
        No1 = No1//10

    return reverse

def main():
    print("Enter a number : ")
    Value = int(input())

    Result = ReverseNo(Value)

    print(Result)

if(__name__ == "__main__"):
    main()        

########################################################
##  Output:
##  Enter a number : 
##  123
##  321
##
##  Enter a number : 
##  5678
##  8765
########################################################    