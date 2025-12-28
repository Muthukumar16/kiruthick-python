# write a python script to print a dictinary which is storing student roll_no as a key and their (name, marks as values).
import json
n = int(input("How much student you want to store: "))
d={}
for i in range (n):
    x= input("Enter roll_no: ")
    y= input("Enter name: ")
    z= input("Enter marks: ")
    d[x]=(y,z)

print(d)
print(json.dumps(d, indent=2))
