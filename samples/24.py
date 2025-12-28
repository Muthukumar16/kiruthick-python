# write a python program to get the frequency of every charectar of a string entered by a user uing 9dictionary!

x= input("Enter a string: ")
d={}

for i in x:
    if i in d:
        d[i]+=1
    else:
        d[i]=1

for j in d:
    if j.isspace():
        continue
    else:
        print(j, 'repets',d[j], 'time(s)')