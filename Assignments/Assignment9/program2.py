########################################################
##  Name : Nidhi Girish Kadival
##  Assignment 9 
##  Question 2
##  Date : 26/06/2026
########################################################

#######################################################################
##
##  Function Name : ChkGreater
##  Description :   It returns Greater number out of the numbers given
##  Input :         int int
##  Output :        int
##  Author :        Nidhi Girish Kadival
##  Date :          26/06/2026
## 
#######################################################################

def ChkGreater(No1, No2):
    if(No1 > No2):
        return No1
    else:
        return No2


def main():
    print("Enter the first number : ")
    Value1 = int(input())

    print("Enter the second number : ")
    Value2 = int(input())

    Result = ChkGreater(Value1,Value2)

    print(Result,"is Greater")

if(__name__ == "__main__"):
    main()        

########################################################
##  Output:
##  Enter the first number : 
##  20
##  Enter the second number : 
##  10
##  20 is Greater
##
##  Enter the first number : 
##  11
##  Enter the second number : 
##  11
##  11 is Greater
########################################################    