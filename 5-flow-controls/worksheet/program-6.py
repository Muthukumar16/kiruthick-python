counts=0
counta=0
countd=0
str1=input("Enter a string:")
str2=str1.replace(" ","")
lstr2=len(str2)
for i in range(0,lstr2):
    if str2[i].isdigit():
        countd+=1
    elif str2[i].isalpha():
        counta+=1
    else:
        counts+=1
print(countd,counta,counts)
