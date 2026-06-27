########################################################
##  Name : Nidhi Girish Kadival
##  Assignment 13
##  Question 4
##  Date : 26/06/2026
########################################################

################################################################################
##
##  Function Name : Binary
##  Description :   It returns the binary equivalent of the given number
##  Input :         int
##  Output :        int
##  Author :        Nidhi Girish Kadival
##  Date :          26/06/2026
## 
################################################################################

def Binary(num):
    binary_num = 0
    place = 1

    while num != 0:
        rem = num % 2
        binary_num = binary_num + rem * place
        place = place * 10
        num = num // 2

    return binary_num    
    
def main():
    print("Enter the number : ")
    Value = int(input())

    Result = Binary(Value)

    print(Result)   

if(__name__ == "__main__"):
    main()        

########################################################
##  Output:
##  Enter the number : 
##  13
##  1101
##
##  Enter the number : 
##  2
##  10
########################################################    