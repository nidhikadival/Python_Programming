########################################################
##  Name : Nidhi Girish Kadival
##  Assignment 12
##  Question 1
##  Date : 26/06/2026
########################################################

#######################################################################
##
##  Function Name : ChckVowel
##  Description :   It prints "Vowel" if the alphabet is a vowel
##  Input :         string
##  Output :        void
##  Author :        Nidhi Girish Kadival
##  Date :          26/06/2026
## 
#######################################################################

def ChckVowel(alpha):
    if(alpha == 'a' or alpha == 'A' or alpha == 'e' or alpha == 'E' or alpha == 'U' or
        alpha == 'i' or alpha == 'I' or alpha == 'o' or alpha == 'O' or alpha == 'u'):
        print("Vowel")
    else:
        print("Not Vowel")      

def main():
    print("Enter an alphabet : ")
    Alphabet = input()

    ChckVowel(Alphabet)

if(__name__ == "__main__"):
    main()        

########################################################
##  Output:
##  Enter an alphabet : 
##  a
##  Vowel
##
##  Enter an alphabet : 
##  h
##  Not Vowel
##
##  Enter an alphabet : 
##  I
##  Vowel
########################################################    