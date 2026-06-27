########################################################
##  Name : Nidhi Girish Kadival
##  Assignment 12
##  Question 5
##  Date : 26/06/2026
########################################################

#######################################################################
##
##  Function Name : PrintReverse
##  Description :   It prints the numbers from the given number to 1
##  Input :         int
##  Output :        void
##  Author :        Nidhi Girish Kadival
##  Date :          26/06/2026
## 
#######################################################################

def PrintReverse(No):
    for i in range(No,0,-1):
        print(i,end=" ")

def main():
    print("Enter a number : ")
    Value = int(input())

    PrintReverse(Value)

if(__name__ == "__main__"):
    main()        

########################################################
##  Output:
##  Enter a number : 
##  5
##  5 4 3 2 1
##                                                                                                                                                                      nidhikadival@Nidhis-MacBook-Air Assignment12 % python3 program4.py
##  Enter a number : 
##  10
##  10 9 8 7 6 5 4 3 2 1   
########################################################    