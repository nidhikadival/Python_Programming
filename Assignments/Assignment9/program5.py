########################################################
##  Name : Nidhi Girish Kadival
##  Assignment 9 
##  Question 5
##  Date : 26/06/2026
########################################################

#################################################################################
##
##  Function Name : Divisible
##  Description :   It returns true if the given number is divisible by 3 & 5
##  Input :         int
##  Output :        int
##  Author :        Nidhi Girish Kadival
##  Date :          26/06/2026
## 
#################################################################################

def Divisible(No1):
    if((No1%3 == 0) and (No1%5 == 0)):
        return True
    else:
        return False    


def main():
    print("Enter a number : ")
    Value = int(input())

    Result = Divisible(Value)

    if(Result == True):
        print("Divisible by 3 & 5")
    else:
        print("Not Divisible by 3 & 5")    

if(__name__ == "__main__"):
    main()        

########################################################
##  Output:
##  Enter a number : 
##  15
##  Divisible by 3 & 5
##
##  Enter a number : 
##  20
##  Not Divisible by 3 & 5
########################################################    