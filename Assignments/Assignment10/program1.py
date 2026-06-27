########################################################
##  Name : Nidhi Girish Kadival
##  Assignment 10
##  Question 1
##  Date : 26/06/2026
########################################################

#######################################################################
##
##  Function Name : Table
##  Description :   It displays multiples of the given input number 
##  Input :         int
##  Output :        void
##  Author :        Nidhi Girish Kadival
##  Date :          26/06/2026
## 
#######################################################################

def Table(No):
    for i in range(1,11):
        print(No*i, end = " ")

def main():
    print("Enter a number :")
    Value = int(input())

    Table(Value)

if(__name__ == "__main__"):
    main()    

########################################################
##  Output:
##  Enter a number :
##  4
##  4 8 12 16 20 24 28 32 36 40 
##                                                                                                                                                  nidhikadival@Nidhis-MacBook-Air Assignment10 % python3 program1.py
##  Enter a number :
##  5
##  5 10 15 20 25 30 35 40 45 50      
########################################################
