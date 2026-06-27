########################################################
##  Name : Nidhi Girish Kadival
##  Assignment 12
##  Question 2
##  Date : 26/06/2026
########################################################

#######################################################################
##
##  Function Name : Factors
##  Description :   It prints the factors of the given number
##  Input :         int
##  Output :        void
##  Author :        Nidhi Girish Kadival
##  Date :          26/06/2026
## 
#######################################################################

def Factors(No):
    for i in range(1,(No+1)):
        if(No%i == 0):
            print(i,end=" ")

def main():
    print("Enter a number : ")
    Value = int(input())

    Factors(Value)

if(__name__ == "__main__"):
    main()        

########################################################
##  Output:
##  Enter a number : 
##  12
##  1 2 3 4 6 12 
##                                                                                                                                                                  nidhikadival@Nidhis-MacBook-Air Assignment12 % python3 program2.py
##  Enter a number : 
##  5
##  1 5    
########################################################    