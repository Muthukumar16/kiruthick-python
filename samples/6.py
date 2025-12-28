# Write a Python program that input a student's marks in five subjects (out of100) and print the percentage.
physics= int(input("Enter your marks in physics: "))
chemistry= int(input("Enter your marks in chemistry: "))
maths= int(input("Enter your marks in maths: "))
computer= int(input("Enter your marks in computer science: "))
english= int(input("Enter your marks in english: "))

total_marks= (physics+ chemistry+ maths+computer+ english)/500
percentage= total_marks*100

print("You scored", percentage, '%')