# Write a menu driven program in Python to print the grade of a student based on the marks.
marks= int(input("Enter your marks: "))

if marks>90 and marks<=100:
    print("Your grade is A+")
elif marks>80 and marks<=90:
    print("Your grade is A")
elif marks>75 and marks<=80:
    print("Your grade is B")
elif marks>60 and marks<=75:
    print("Your grade is C")
elif marks>50 and marks<=60:
    print("Your grade is D")
elif marks>0 and marks<=50:
    print("Your grade is E")
else:
    print("Wrong input")
