# Write a Python program that input a student's marks in five subjects (out of100) and print the percentage.
physics= eval(input("Enter your marks in physics: "))
chemistry= eval(input("Enter your marks in chemistry: "))
maths= eval(input("Enter your marks in maths: "))
computer= eval(input("Enter your marks in computer science: "))
english= eval(input("Enter your marks in english: "))

total_marks= (physics+ chemistry+ maths+computer+ english)/500
percentage= total_marks*100

print("You scored", percentage, '%')