########################################################
##  Name : Nidhi Girish Kadival
##  Assignment 11
##  Question 1
##  Date : 26/06/2026
########################################################

#######################################################################
##
##  Function Name : Prime
##  Description :   It returns true if number is true 
##  Input :         int
##  Output :        bool
##  Author :        Nidhi Girish Kadival
##  Date :          26/06/2026
## 
#######################################################################

def Prime(No1):
    if(No1 <= 1):
        return False
    elif(No1 == 2):
        return True    
    else:
        for i in range(2,(No1+1)):
            if(No1%i == 0):
                return False
            else:
                return True    

def main():
    print("Enter a number : ")
    Value = int(input())

    Result = Prime(Value)

    if(Result == True):
        print("Prime Number")
    else:
        print("Not Prime")    

if(__name__ == "__main__"):
    main()        

########################################################
##  Output:
##  Enter a number : 
##  5
##  Prime Number
##
##  Enter a number : 
##  10
##  Not Prime
##
##  Enter a number : 
##  2
##  Prime Number
########################################################    