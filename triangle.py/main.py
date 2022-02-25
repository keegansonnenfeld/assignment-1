
#the triangle sides
a = float(input("Enter the first side: "))
b = float(input("Enter the second side: "))
c = float(input("Enter the third side: "))
print("")
#Compute the sides
if ((a**2 == b**2 + c**2) or (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2)):
    print("The triangle is a right triangle.")
else:
    print("The triangle is not a right triangle.")
    # _Check for equilateral triangle
    if ( a == b == c):
        print("The triangle is equilateral triangle")
