from cs50 import get_int

n= get_int("Height: ")
if (n<1  or n >8):
 print("Incorrect value")
else:

 for i in range(n):
    print(" "*(n-1-i),"#"*(i+1))
        
 print()