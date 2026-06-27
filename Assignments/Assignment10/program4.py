########################################################
##  Name : Nidhi Girish Kadival
##  Assignment 10
##  Question 4
##  Date : 26/06/2026
########################################################

#######################################################################
##
##  Function Name : EvenNumbers
##  Description :   It displays all the even numbers till the given no
##  Input :         int
##  Output :        void
##  Author :        Nidhi Girish Kadival
##  Date :          26/06/2026
## 
#######################################################################

def EvenNumbers(No):

    for i in range(1,(No+1)):
        if(i%2 == 0):
            print(i, end=" ")
  

def main():
    print("Enter a number :")
    Value = int(input())

    EvenNumbers(Value)

if(__name__ == "__main__"):
    main()    

########################################################
##  Output:
##  Enter a number :
##  10  
##  2 4 6 8 10 
##                                                                                                                                                                         nidhikadival@Nidhis-MacBook-Air Assignment10 % python3 program4.py
##  Enter a number :
##  20
##  2 4 6 8 10 12 14 16 18 20   
########################################################
