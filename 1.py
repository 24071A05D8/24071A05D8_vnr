#check prime or not
x= int (input("Enter number: "))
i=2
flag=0
while(i<x):
    if(x%i==0):
        flag=1
        break
    i+=1
if flag==1:
    print(str (x)+ " is not a prime")
else:
    print(str (x)+" is prime")