########################################################
##  Name : Nidhi Girish Kadival
##  Assignment 2 
##  Question 2
##  Date : 13/06/2026
########################################################

a = 2
b = 2

print("Memory Address of a is : ",id(a))
print("Memory Address of b is : ",id(b))

print()

a = [10]
b = [10]

print("Memory Address of a is : ",id(a))
print("Memory Address of b is : ",id(b))

print("Diferent Integers may share the same memory location,")
print("while separate List objects have different memory locations")
print("even if their contents are same.")

########################################################
##  Output:
##  Memory Address of a is :  4322258944
##  Memory Address of b is :  4322258944
##
##  Memory Address of a is :  4299200832
##  Memory Address of b is :  4299409920
##
##  Diferent Integers may share the same memory location,
##  while separate List objects have different memory locations
##  even if their contents are same.
########################################################
