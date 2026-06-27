########################################################
##  Name : Nidhi Girish Kadival
##  Assignment 11
##  Question 5
##  Date : 26/06/2026
########################################################

#######################################################################
##
##  Function Name : Palindrome
##  Description :   It returns True if number is a Palindrome
##  Input :         int
##  Output :        bool
##  Author :        Nidhi Girish Kadival
##  Date :          26/06/2026
## 
#######################################################################

def Palindrome(No1):
    num = No1
    reverse = 0

    while(No1 != 0):
        digit = No1%10
        reverse = reverse*10 + digit
        No1 = No1//10

    if(reverse == num):
        return True
    else:
        return False    

def main():
    print("Enter a number : ")
    Value = int(input())

    Result = Palindrome(Value)

    if(Result == True):
        print("Palindrome")
    else:
        print("Not a Palindrome")    

if(__name__ == "__main__"):
    main()        

########################################################
##  Output:
##  Enter a number : 
##  121
##  Palindrome
##
##  Enter a number : 
##  123
##  Not a Palindrome
########################################################    