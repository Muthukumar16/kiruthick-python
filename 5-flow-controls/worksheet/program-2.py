num1=int(input("Enter starting Range"))
num2=int(input("Enter end Range"))
summ=0
for i in range(num1,num2):
    if num1%2==1:    
        summ+=num1
    num1+=1
print(summ)
