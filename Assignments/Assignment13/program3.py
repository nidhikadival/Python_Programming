########################################################
##  Name : Nidhi Girish Kadival
##  Assignment 13
##  Question 3
##  Date : 26/06/2026
########################################################

#######################################################################
##
##  Function Name : ChkPerfect
##  Description :   It returns True if No is Perfect
##  Input :         int
##  Output :        bool
##  Author :        Nidhi Girish Kadival
##  Date :          26/06/2026
## 
#######################################################################

def ChkPerfect(No):
    sum = 0
    for i in range(1,No):
        if(No%i == 0):
            sum = sum + i

    if(sum == No):
        return True
    else:
        return False           
    

def main():
    print("Enter the number : ")
    Value = int(input())

    Result = ChkPerfect(Value)

    if(Result == True):
        print("Perfect Number")
    else:
        print("Not a Perfect Number")    

if(__name__ == "__main__"):
    main()        

########################################################
##  Output:
##  Enter the number : 
##  6
##  Perfect Number
##
##  Enter the number : 
##  4
##  Not a Perfect Number
########################################################    