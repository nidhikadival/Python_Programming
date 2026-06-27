########################################################
##  Name : Nidhi Girish Kadival
##  Assignment 10
##  Question 5
##  Date : 26/06/2026
########################################################

#######################################################################
##
##  Function Name : OddNumbers
##  Description :   It displays all the odd numbers till the given no
##  Input :         int
##  Output :        void
##  Author :        Nidhi Girish Kadival
##  Date :          26/06/2026
## 
#######################################################################

def OddNumbers(No):

    for i in range(1,(No+1)):
        if(i%2 != 0):
            print(i, end=" ")
  

def main():
    print("Enter a number :")
    Value = int(input())

    OddNumbers(Value)

if(__name__ == "__main__"):
    main()    

########################################################
##  Output:
##  Enter a number :
##  10
##  1 3 5 7 9          
##                                                                                                                                                                 nidhikadival@Nidhis-MacBook-Air Assignment10 % python3 program5.py
##  Enter a number :
##  20
##  1 3 5 7 9 11 13 15 17 19  
########################################################
