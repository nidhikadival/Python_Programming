########################################################
##  Name : Nidhi Girish Kadival
##  Assignment 12
##  Question 4
##  Date : 26/06/2026
########################################################

#######################################################################
##
##  Function Name : PrintNumbers
##  Description :   It prints the numbers from 1 to the given number
##  Input :         int
##  Output :        void
##  Author :        Nidhi Girish Kadival
##  Date :          26/06/2026
## 
#######################################################################

def PrintNumbers(No):
    for i in range(1,(No+1)):
        print(i,end=" ")

def main():
    print("Enter a number : ")
    Value = int(input())

    PrintNumbers(Value)

if(__name__ == "__main__"):
    main()        

########################################################
##  Output:
##  Enter a number : 
##  5
##  1 2 3 4 5 
##                                                                                                                                                                      nidhikadival@Nidhis-MacBook-Air Assignment12 % python3 program4.py
##  Enter a number : 
##  10
##  1 2 3 4 5 6 7 8 9 10   
########################################################    