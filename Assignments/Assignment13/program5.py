########################################################
##  Name : Nidhi Girish Kadival
##  Assignment 13
##  Question 5
##  Date : 26/06/2026
########################################################

################################################################################
##
##  Function Name : Grade
##  Description :   It displays grade based on marks
##  Input :         int
##  Output :        void
##  Author :        Nidhi Girish Kadival
##  Date :          26/06/2026
## 
################################################################################

def Grade(marks):
    if(marks >= 75):
        print("Distinction")
    elif(marks >= 60):
        print("First Class")
    elif(marks >= 50):
        print("Second Class")
    else:
        print("Fail")              
    
def main():
    print("Enter marks : ")
    Value = int(input())

    Grade(Value)   

if(__name__ == "__main__"):
    main()        

########################################################
##  Output:
##  Enter marks : 
##  70
##  First Class
##
##  Enter marks : 
##  90
##  Distinction
##
##  Enter marks : 
##  40
##  Fail
##
##  Enter marks : 
##  55
##  Second Class
########################################################    